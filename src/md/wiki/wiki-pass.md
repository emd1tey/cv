This code provides instructions for changing the root password in MySQL for version 5.7 and above.

1. Stop MySQL service:
на 5.7+

1. Stop mysql:\
''systemctl stop mysqld''

2. Set the mySQL environment option
''systemctl set-environment MYSQLD_OPTS="--skip-grant-tables"''

3. Start mysql usig the options you just set
''systemctl start mysqld''

4. Login as root
''mysql -u root''

5. Update the root user password with these mysql commands
''mysql> UPDATE mysql.user SET authentication_string = PASSWORD('MyNewPassword')
    -> WHERE User = 'root' AND Host = 'localhost';
mysql> FLUSH PRIVILEGES;
mysql> quit''

*** Edit ***
As mentioned my shokulei in the comments, for 5.7.6 and later, you should use
''   mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';''
Or you'll get a warning

6. Stop mysql
''systemctl stop mysqld''

7. Unset the mySQL envitroment option so it starts normally next time
''systemctl unset-environment MYSQLD_OPTS''

8. Start mysql normally:\
''systemctl start mysqld''

Try to login using your new password:\
7. ''mysql -u root -p''
