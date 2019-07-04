FROM python:3.6

RUN pip install -r requirements.txt
WORKDIR /app
COPY app /app

CMD ["python", "identidock.py"]