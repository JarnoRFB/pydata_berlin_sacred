FROM python:3.6-jessie

RUN apt update \
   && pip install https://github.com/chovanecm/sacredboard/archive/develop.zip \
   && rm -rf /var/lib/apt/lists/*

ENTRYPOINT sacredboard -m $MONGO_DATABASE
