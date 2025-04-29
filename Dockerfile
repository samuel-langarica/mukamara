FROM python:3.9-slim

WORKDIR /app
COPY build/web /app/build/web
COPY server.py .

EXPOSE 8080

CMD ["python", "server.py"] 