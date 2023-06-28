# Пульт охраны банка

Репозитарий представляет собой веб-интерфейс для контроля посещаемости хранилища банка. 


### Как установить

#### Переменные окружения:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

```
.
├── .env
└── manage.py
```
Обязательные переменные:
- `DB_ENGINE` - зависит от типа используемой базы данных, см. https://docs.djangoproject.com/en/4.0/ref/databases/
- `DB_HOST` - хост используемый для подключения к базе данных, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-HOST
- `DB_PORT` - порт используемый при подключении к базе данных, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-PORT
- `DB_NAME` - имя используемой базы данных, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-NAME
- `DB_USER` - имя пользователя, используемое при подключении к базе данных, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-USER
- `DB_PASSWORD` - пароль используемый при подключении к базе данных, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-PASSWORD
- `SECRET_KEY` - секретный ключ для конкретной установки Django. (добавляется автоматический при создании нового проекта), см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-SECRET_KEY
- `DEBUG` - логическое значение, которое включает/выключает режим отладки, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-DEBUG
- `ALLOWED_HOSTS` - список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django, см. https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-ALLOWED_HOSTS

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

### Пример запуска

Скрипты работают из консольной утилиты.

Запуск скрипта: ```python manage.py runserver 0.0.0.0:8000```

Доступ к веб-интерфейсу http://127.0.0.1:8000/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).