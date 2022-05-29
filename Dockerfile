# образ на основе которого создаём контейнер
FROM python:3.9.10-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/bathrobe/

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN python -m pip install --upgrade pip setuptools wheel
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY bathrobe /usr/src/bathrobe/

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_USERNAME
fi

$@