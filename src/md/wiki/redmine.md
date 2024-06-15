#  Установка

###  nginx настройки

####  подкидываем thin:
''vim /usr/local/share/redmine/Gemfile'' , после rails докидываем это ГЕМ ''gem "thin"'',
из директории где находится подтягиваем все что надо командой:\
''bundle install --without development test postgresql sqlite''(БД по выбору, по умолчанию MySQL)

Тут смотреть конфиг конекта к базе config/database.yml

тестовый сервак на 3000 порту проверить кто ебется nginx или рэдмайн
''ruby bin/rails server webrick -e production -b 0.0.0.0''

Конфиги nginx на гите или гуглить

Ссыль по которой ставил первый раз, с новыми версиями все то же самое

https://mihanentalpo.me/2018/04/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-redmine-nginx-thin-%D0%BD%D0%B0-debian-9-stretch/
