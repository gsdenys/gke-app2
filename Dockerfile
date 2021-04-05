FROM python:3-alpine

RUN apk add --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            musl-dev \
            postgresql-dev \
            pcre-dev \
            libpq \
            pcre
            
COPY /app /app

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 3000

CMD ["uwsgi", "--ini", "wsgi.ini"]