Настройка и тюнинг DNS сервера BIND9 может быть сложной задачей, но с правильным планом это станет более управляемым процессом. Вот подробный список действий (TODO) для установки, настройки и тюнинга BIND9, а также меры по DRP (Disaster Recovery Plan).

### TODO: Установка и настройка BIND9

1. **Установка BIND9**
    - Обновите список пакетов и установите BIND9:
      ```bash
      sudo apt update
      sudo apt install bind9 bind9utils bind9-doc
      ```

2. **Конфигурация основного (авторитетного) DNS сервера**

    - Настройте файл конфигурации `/etc/bind/named.conf.options`:
      ```bash
      options {
          directory "/var/cache/bind";
          recursion no;
          allow-transfer { none; }; // Disable zone transfers by default
          dnssec-validation auto;
          auth-nxdomain no;    # conform to RFC1035
          listen-on { any; };
          allow-query { any; };
      };
      ```

    - Настройте зоны в `/etc/bind/named.conf.local`:
      ```bash
      zone "example.com" {
          type master;
          file "/etc/bind/db.example.com";
          allow-transfer { 192.0.2.2; }; // IP подчиненного сервера
      };
      ```

    - Создайте зону файла `/etc/bind/db.example.com`:
      ```bash
      $TTL 86400
      @   IN  SOA ns1.example.com. admin.example.com. (
              2024061501 ; Serial
              3600       ; Refresh
              1800       ; Retry
              604800     ; Expire
              86400 )    ; Minimum TTL
      @   IN  NS  ns1.example.com.
      @   IN  NS  ns2.example.com.
      ns1 IN  A   192.0.2.1
      ns2 IN  A   192.0.2.2
      www IN  A   192.0.2.3
      ```

3. **Конфигурация подчиненного DNS сервера**

    - Настройте файл конфигурации `/etc/bind/named.conf.options` аналогично основному серверу.

    - Настройте зоны в `/etc/bind/named.conf.local`:
      ```bash
      zone "example.com" {
          type slave;
          file "/var/cache/bind/db.example.com";
          masters { 192.0.2.1; }; // IP авторитетного сервера
      };
      ```

4. **Перезагрузка и проверка конфигурации**

    - Перезапустите BIND9 на обоих серверах:
      ```bash
      sudo systemctl restart bind9
      ```

    - Проверьте конфигурацию:
      ```bash
      sudo named-checkconf
      sudo named-checkzone example.com /etc/bind/db.example.com
      ```

### Тюнинг BIND9

1. **Увеличение производительности**
    - Включите `RNDC` для управления сервером:
      ```bash
      sudo rndc-confgen -a
      ```
      Добавьте RNDC ключи в конфигурацию `/etc/bind/named.conf`:
      ```bash
      include "/etc/bind/rndc.key";

      controls {
          inet 127.0.0.1 port 953
              allow { 127.0.0.1; } keys { "rndc-key"; };
      };
      ```

    - Оптимизируйте параметры кеширования:
      ```bash
      options {
          max-cache-size 128M; // Set max cache size
          max-ncache-ttl 3600; // Negative cache TTL
          min-ncache-ttl 1800; // Minimum negative cache TTL
      };
      ```

2. **Безопасность**
    - Включите DNSSEC:
      ```bash
      options {
          dnssec-enable yes;
          dnssec-validation yes;
      };
      ```

    - Ограничьте доступ к серверу:
      ```bash
      allow-transfer { none; }; // Disable zone transfers by default
      ```

3. **Мониторинг и логирование**
    - Включите расширенное логирование:
      ```bash
      logging {
          channel default_log {
              file "/var/log/named/named.log" versions 3 size 5m;
              severity info;
              print-time yes;
              print-severity yes;
              print-category yes;
          };
          category default { default_log; };
      };
      ```

### Disaster Recovery Plan (DRP)

1. **Резервное копирование конфигурации**
    - Настройте регулярное резервное копирование файлов конфигурации и зоны:
      ```bash
      crontab -e
      # Добавьте следующее:
      0 2 * * * /usr/bin/rsync -a /etc/bind /backup/bind-$(date +\%Y\%m\%d)
      ```

2. **Тестирование резервных копий**
    - Регулярно тестируйте восстановление из резервных копий на тестовом сервере.

3. **Автоматическое переключение на подчиненный сервер**
    - Убедитесь, что подчиненный сервер настроен правильно и может принять трафик в случае сбоя основного сервера.

4. **Документация**
    - Поддерживайте документацию о конфигурации и процедурах восстановления.

### Заключение

Этот план охватывает основные этапы установки и настройки BIND9, а также включает тюнинг для повышения производительности и безопасности. Регулярное резервное копирование и тестирование DRP поможет минимизировать время простоя в случае аварийной ситуации.
