Liscense server - http://idea.imsxm.com/

________________________________________________________________

ЗАПУСК
________________________________________________________________


Terminal 1:
-Запуск локального сервера
py devmanage.py runserver


________________________________________________________________

УСТАНОВКА
________________________________________________________________

-Settings -> Project: -> Project Interpreter - python.exe

-Создание и запуск виртуального окружения:
py -m venv wsenv

-Settings -> Project: -> Project Interpreter -> wsenv

-Устнаовка плагинов:
pip install django

-Создание devsettings.py, devurls.py, devmanage.py, secret.py

-Добавление настроек в settings.py

-Создание приложения, если оно не создано
py manage.py startapp main

-Создать файл main/urls.py

-В main/urls.py импортируем views.py

-В main/views.py  создаем функцию main

-В папке templates создаем папку main и в ней файл index.html

-В папке templates создаем файл base.html, header.html, footer.html ...

-
















-Скачать nodejs

-Инициализация:
npm init  		# создание package.json

-Установка:
npm i -g gulp bower

-Сохранение в package.json:
npm i gulp --save-dev	        # создание node_modules

-Сохранение в package.json плагинов:
npm i gulp-sass gulp-concat gulp-uglify-es gulp-clean-css gulp-rename gulp-autoprefixer gulp-notify gulp-livereload --save-dev

-Скачать git

-Скачивание библиотек:
bower i jquery bootstrap components-font-awesome --save


________________________________________________________________

ДОПОЛНИТЕЛЬНО
________________________________________________________________

-Команды Django:
py devmanage.py makemigrations
py devmanage.py migrate
py devmanage.py createsuperuser
py devmanage.py dumpdata > dump.json
py devmanage.py loaddata dump.json

-Создать requirements.txt:
pip freeze > requirements.txt

-Установить пакеты из requirements.txt:
pip install -r requirements.txt