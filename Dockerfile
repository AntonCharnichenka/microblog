FROM python:3.6-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt
RUN pip install gunicorn pymysql

COPY ./app ./app
COPY ./migrations ./migrations
COPY ./microblog.py ./config.py ./boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
