FROM python:3
WORKDIR /usr/src/app
RUN pip install psutil
COPY app.py /usr/src/app
CMD python app.py
