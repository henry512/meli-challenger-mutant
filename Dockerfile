FROM python:3.8.5-slim-buster

COPY . /app
WORKDIR /app

RUN pip install wheel gunicorn gevent && pip install -r requirements/base.txt 

EXPOSE 5000
CMD ["python", "-u" , "main.py", "runserver"]
# CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "manage:app"]