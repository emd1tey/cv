# Простая настройка связки NGINX и FFmpeg для RTMP

## Установка

1. Установите необходимые пакеты `nginx`, `libnginx-mod-rtmp` и `ffmpeg` с помощью команды:
   ```bash
   sudo apt install nginx libnginx-mod-rtmp ffmpeg
   ```

2. Добавьте в конфигурационный файл NGINX контекст `rtmp`.

## Конфигурация NGINX

Откройте конфигурационный файл NGINX для редактирования:
```bash
sudo nano /etc/nginx/nginx.conf
```

Добавьте следующие настройки в конфигурационный файл:

### 2.1. Ретрансляция готового потока RTSP

```nginx
rtmp {
    server {
        listen 1935;

        application rtsp {
            live on;
            exec_static /usr/bin/ffmpeg -i rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov -c copy -f flv rtmp://localhost/rtsp/stream;
        }
    }
}
```

### 2.2. Конвертация видео в RTMP и трансляция

```nginx
rtmp {
    server {
        listen 1935;

        application mp4 {
            live on;
            exec_pull /usr/bin/ffmpeg -re -i /var/www/html/big_buck_bunny_720p_30mb.mp4 -c copy -f flv rtmp://localhost/mp4/stream;
        }
    }
}
```

### 2.3. Трансляция с веб-камеры

#### Конфигурация NGINX

```nginx
rtmp {
    server {
        listen 1935;

        application webcam {
            live on;
        }
    }
}
```

#### Запуск трансляции с компьютера, где подключена веб-камера

Запустите команду FFmpeg:
```bash
ffmpeg -i /dev/video0 -video_size 720x404 -vcodec libx264 -maxrate 768k -bufsize 8080k -vf "format=yuv420p" -g 60 -f flv rtmp://localhost/webcam/stream
```

## Перезапуск NGINX

После внесения изменений в конфигурационный файл NGINX, перезапустите службу:
```bash
sudo systemctl restart nginx
```

## Дополнительные рекомендации

1. **Защита потоков**: Для обеспечения безопасности ваших потоков, рекомендуется настроить аутентификацию и авторизацию, чтобы ограничить доступ к трансляциям.

2. **Мониторинг и логирование**: Настройте мониторинг и логирование, чтобы отслеживать производительность сервера и оперативно реагировать на возможные проблемы.

3. **Тестирование и отладка**: Перед запуском в продакшен, тщательно протестируйте все сценарии трансляций и убедитесь, что все работает корректно.

Эти шаги помогут вам быстро и эффективно настроить простую систему потокового вещания с использованием NGINX и FFmpeg.
