FROM python:3.6

ENV ELASTICSEARCH_URL="http://elastic:9200"
ENV MONGODB_URI="mongodb://mongo:27017"

RUN mkdir /code
WORKDIR /code

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
