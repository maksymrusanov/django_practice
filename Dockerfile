FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запуск через gunicorn
CMD ["gunicorn", "movie_adviser.wsgi:application", "--bind", "0.0.0.0:8000"]

