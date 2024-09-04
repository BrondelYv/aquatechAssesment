 
# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
RUN ./process.sh