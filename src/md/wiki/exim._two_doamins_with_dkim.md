log_file_path = syslog : /var/log/exim4/%slog - путь к лог-файлу
primary_hostname = bagna.of.by  -название локал-хоста(необязательный параметр)
local_interfaces = 127.0.0.1 - не рилэйм откуда-попало.

daemon_smtp_ports = 25 : 465

disable_ipv6 = true
queue_run_max = 100
smtp_accept_max = 100
smtp_connect_backlog = 20
smtp_accept_max_per_connection = 20
smtp_accept_max_per_host = 20
smtp_accept_queue_per_connection = 20
smtp_accept_queue = 25

# The next three settings create two lists of domains and one list of hosts.
# These lists are referred to later in this configuration using the syntax
# +local_domains, +relay_to_domains, and +relay_from_hosts, respectively. They
# are all colon-separated lists:
# If you are using MySQL, uncomment the following two lines:

domainlist local_domains = iknow.of.by : bagna.of.by # списки доменов, которые могут отправлять с данного сервера
domainlist relay_to_domains = iknow.of.by : bagna.of.by # почтовые домены, которые могут рилэйть
hostlist   relay_from_hosts = localhost
trusted_users = Debian-exim:list #  пользователи, от которых могут отправлятся сообщения
domainlist washer_domains = iknow.of.by : bagna.of.by #

exim_user = Debian-exim # пользователь от которого работает  exim
exim_group = Debian-exim # группа
never_users = root # пользователь от которых не отправлять письма

host_lookup = *
rfc1413_hosts = *
rfc1413_query_timeout = 0s

ignore_bounce_errors_after = 9d
timeout_frozen_after = 9d

log_selector = +subject

######################################################################
#                       ACL CONFIGURATION                            #
#         Specifies access control lists for incoming SMTP mail      #
# В этом блоке формируем списки от кого можем принимать почту,а от   #
# кого нет. Это деалется, чтобы исключить спамеров                   #
######################################################################

begin acl

acl_check_helo:

acl_check_rcpt:

 accept  hosts = :

 deny authenticated = *
  ratelimit = 60 / 1h / leaky / $authenticated_id
  message = Only $sender_rate_limit letters per $sender_rate_period is allowed, while your rate is $sender_rate

  accept  authenticated = *

  deny    local_parts   = ^.*[@%!/|] : ^.

  accept  local_parts   = postmaster
          domains       = +local_domains

  # Accept if the address is in a local domain, but only if the recipient can
  # be verified. Otherwise deny. The "endpass" line is the border between
  # passing on to the next ACL statement (if tests above it fail) or denying
  # access (if tests below it fail).

  accept  domains       = +local_domains
          endpass
          verify        = recipient

  # Accept if the address is in a domain for which we are relaying, but again,
  # only if the recipient can be verified.

  accept  domains       = +relay_to_domains
          endpass
          verify        = recipient

  accept  domains       = +washer_domains
          endpass
          verify        = recipient

  deny    message       = relay not permitted

acl_check_content:

  accept

######################################################################
#                      ROUTERS CONFIGURATION                         #
#               Specifies how addresses are handled                  #
######################################################################
#     THE ORDER IN WHICH THE ROUTERS ARE DEFINED IS IMPORTANT!       #
# An address is passed to each router in turn until it is accepted.  #
#Настраиваем роуты отправки писем                                    #
######################################################################

begin routers

dnslookup:
  driver = dnslookup
  domains = ! +local_domains
  transport = remote_smtp
  ignore_target_hosts = 0.0.0.0 : 127.0.0.0/8
  no_more

blackholes:
  driver = redirect
  allow_fail
  check_local_user
  data = :blackhole:

######################################################################
#                      TRANSPORTS CONFIGURATION                      #
######################################################################
#                       ORDER DOES NOT MATTER                        #
#     Only one appropriate transport is called for each delivery.    #
#Настраиваем транспорт отпраки. Т.е. как сообщение формируется, что с#
#                ним при отправке делаем, что делаем при получении   #
######################################################################

begin transports

remote_smtp:
  driver = smtp
  dkim_domain = ${lc:${domain:$h_from:}} # берем домен из заголовка from
  dkim_selector = mail #dkim selector(для txt записи) пример: mail._domainkey.bagna.of.by. v=DKIM1; k=rsa; t=s;  p=MIGfMA0GCSqGSIb3DQE
  dkim_private_key = ${if exists {/etc/exim4/dkim/$dkim_selector.$dkim_domain.private}
                                {/etc/exim4/dkim/$dkim_selector.$dkim_domain.private}{}}  # Выбираем приватный ключ для подписи в зависиомсти от домена

Дальше настройки в зависимости от того как почту принимаем.
