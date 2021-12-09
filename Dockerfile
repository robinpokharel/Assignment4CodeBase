@ Dockerfile
FROM ubuntu

RUN apt update && apt install -y python3-pip 
@RUN pip -r
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "./app.py"]
