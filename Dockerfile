FROM python:3.13.0a4-slim
LABEL  maintainer "Yuki Nagae <yuki.nagae1130@gmail.com>"
ENV TZ Asia/Tokyo

RUN mkdir /api
WORKDIR /api

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential curl

RUN pip install --upgrade setuptools && \
    pip install pipenv

ADD . .

# Install dependencies on system (virtual env is not necessary anymore)
# see: https://qiita.com/sabaku20XX/items/8bc6e8f999e8009d76fd
RUN pipenv install --system

EXPOSE 8080

CMD nameko run --config config.yaml app.api
