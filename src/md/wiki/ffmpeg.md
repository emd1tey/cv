# Голая лайтовая связка nginx + ffmpeg

## Установка

1. Установите пакеты `nginx`, `libnginx-mod-rtmp` и `ffmpeg` с помощью команды:

apt install nginx  libnginx-mod-rtmp ffmpeg

2. Ну и добавляем в конфиг nginx контекст rtmp

2.1. Ретрансляция котового потока rtcp:\

        application rtsp {
            exec_static /usr/bin/ffmpeg -i rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov -c copy -f flv rtmp://185.179.83.97/rtsp/stream;
	    live on;
        }

2.2. Конвертация видоса в ртмп и трансляция:\

	application mp4 {
            exec_pull /usr/bin/ffmpeg -re -i /var/www/html/big_buck_bunny_720p_30mb.mp4 -c copy -f flv rtmp://185.179.83.97/mp4/stream;
	    live on;
	}

2.3. Вебкам трансляция:\
В nginx:\

	application webcam {
	    live on;
	}
С компа где подключена вебка:\

''ffmpeg -i /dev/video0 -video_size 720x404 -vcodec libx264 -maxrate 768k -bufsize 8080k -vf "format=yuv420p" -g 60 -f flv rtmp://185.179.83.97/webcam/stream''