FROM python:3.6

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==1.0.3 uwsgi==2.0.18
WORKDIR /app
COPY app /app

EXPOSE 9090 9191
USER uwsgi

CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", "--callable", "app", "--stats", "0.0.0.0:9191"]