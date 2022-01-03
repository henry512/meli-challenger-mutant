FROM python:3.8.5-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install wheel && pip install -r requirements/production.txt
RUN pip install -r gunicorn gevent

EXPOSE 5000
CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "main:app"]