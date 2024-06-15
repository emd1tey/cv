#  Сбор информации о DNS сервере при использовании CHAOS

###  1) Узнаем версию dns пакета на сервере
С помощью данного запроса можно определить версию пакета не только для bind, но и для других серверов.
Для определения версии dns сервера, если она не скрыта, необходимо формирать следующий запрос:\
* **dig @ns_server chaos txt version.bind **  еще можно использовать version.server( некоторые ответят, некоторые нет т.к. не станртизрована. NSD к примеру отвечает.)

Пример с положительным ответом(UPD написал мише - скрыли, ответ теперь другой):\
    - Узнаем какой dns сервер отвечает за зону:\
dig ns hosterby.com

;; ANSWER SECTION:\

hosterby.com.           600     IN      NS      ns1.hosterby.com.
hosterby.com.           600     IN      NS      ns2.hosterby.com.

    - Формирум запрос для уточнения версии dns зоны:\
** dig @ns1.hosterby.com chaos txt version.bind**

; <<>> DiG 9.16.1 <<>> chaos txt version.bind @ns1.hosterby.com
;; global options: +cmd
;; Got answer:\
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 32614
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:\
; EDNS: version: 0, flags:; udp: 1680
;; QUESTION SECTION:\
;version.bind.                  CH      TXT

;; ANSWER SECTION:\
**version.bind.           5       CH      TXT     "PowerDNS Authoritative Server 4.1.6"**

;; Query time: 996 msec
;; SERVER: 93.125.31.240#53(93.125.31.240)
;; WHEN: Wed Apr 01 15:09:35 +03 2020
;; MSG SIZE  rcvd: 89

Из инетересного на @dns1.tld.tutby.com. - также не закрыты версии dns  серверов:\
**version.bind.           0       CH      TXT     "9.9.5-9+deb8u18-Debian"**

    - Ответ со скрытой версией DNS сервера:\

dig chaos txt version.bind @u1.hoster.by

; <<>> DiG 9.16.1 <<>> chaos txt version.bind @u1.hoster.by
;; global options: +cmd
;; Got answer:\
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25846
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:\
; EDNS: version: 0, flags:; udp: 1680
;; QUESTION SECTION:\
;version.bind.                  CH      TXT

;; ANSWER SECTION:\
version.bind.           5       CH      TXT     "PowerDNS"

;; Query time: 106 msec
;; SERVER: 93.125.30.201#53(93.125.30.201)
;; WHEN: Wed Apr 01 15:23:32 +03 2020
;; MSG SIZE  rcvd: 62

###  2) Использование CHAOS для уточнения точного hostname

Данная информация необходима для уточнения точного hostname сервера. Пример - высоконагрженные сервера, которые имеют одинаковый ip адрес и распределены по миру. При обращению к нему мы попадаем на ближайший. Это возможно при реализации "anycast routing". Система маршрутизации находит ближайший к тебе экземпляр. К примеру это корневые DNS сервера.
**Запрос dig @ns_server chaos txt hostname.bind**
Пример:\
dig @l.root-servers.net. chaos txt hostname.bind  , либо id.server в конце(стандратизирована по RFC  поддерживает BIND)

; <<>> DiG 9.16.1 <<>> @l.root-servers.net. chaos txt hostname.bind
; (2 servers found)
;; global options: +cmd
;; Got answer:\
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52806
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:\
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:\
;hostname.bind.                 CH      TXT

;; ANSWER SECTION:\
hostname.bind.          0       CH      TXT     "aa.by-gme.l.root"

;; Query time: 10 msec
;; SERVER: 199.7.83.42#53(199.7.83.42)
;; WHEN: Wed Apr 01 16:40:04 +03 2020
;; MSG SIZE  rcvd: 71
