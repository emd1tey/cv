Для определения версии dns сервера, если она не скрыта запрос необходимо формирать следующий запрос:\
* **dig @ns_server version.bind txt chaos**

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
