FROM python:3.9-slim

RUN apt-get update && apt-get install -y make

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt --no-cache-dir

CMD ["make", "start_script"]
