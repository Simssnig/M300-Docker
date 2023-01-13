FROM python:3
WORKDIR /usr/src/app
RUN python3 install psutil
RUN python3 install pymongo
COPY app.py /usr/src/app
CMD python app.py
