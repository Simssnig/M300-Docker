FROM python:3.7-alpine

RUN pip install psutil

COPY . /

CMD python app.py
