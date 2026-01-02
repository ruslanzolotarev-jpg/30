# Используем базовую Python-образ с нужной версией
FROM python:3.12-slim-buster

# Устанавливаем необработанный вывод Python для лучшего взаимодействия с контейнером
ENV PYTHONUNBUFFERED=1

# Рабочая директория приложения
WORKDIR /app

# Обновляем Pip и устанавливаем Poetry
RUN pip install --upgrade pip \
    && pip install "poetry==1.5.1"

# Настраиваем Poetry, чтобы он не создавал виртуальное окружение
RUN poetry config virtualenvs.create false --local

# Копируем зависимости перед кодом приложения
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с использованием Poetry
RUN poetry install --no-root

# Копируем весь исходный код нашего Django-приложения
COPY mysite .

# Запускаем сервер Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "mysite.wsgi:application"]
