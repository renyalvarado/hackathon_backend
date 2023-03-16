# create dockerfile for project
FROM ubuntu:latest
# merge next run lines into a single one
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3", "main.py"]
