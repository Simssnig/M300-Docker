FROM python:3
WORKDIR /usr/src/app
RUN python3 -m pip install psutil
RUN python3 -m pip install pymongo
COPY app.py /usr/src/app
CMD python app.py
