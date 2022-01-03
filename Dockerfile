FROM python:3.8.5-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y pip3
RUN pip3 install wheel && pip3 install -r requirements/production.txt

EXPOSE 5000
CMD ["python", "-u" , "main.py", "runserver"]