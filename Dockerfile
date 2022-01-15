FROM python:3.8.5-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install wheel gunicorn==20.1.0 gevent==21.12.0 && pip install -r requirements/production.txt

EXPOSE 5000
CMD ["python", "main.py", "runserver"]
#CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "main:app"]
