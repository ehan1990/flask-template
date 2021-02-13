FROM python:3.8-alpine

RUN apk add --no-cache bash \
                       curl \
                       nano

WORKDIR /app

COPY libs libs
COPY common common
COPY routes routes
COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]

