FROM python:alpine

RUN pip install fastapi-cli

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "fastapi","run" ]