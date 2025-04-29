# Mukamara

A Flutter web application containerized with Docker.

## Prerequisites

- Flutter SDK
- Docker

## Building and Running Locally

1. Build the Flutter web app:
```bash
flutter build web
```

2. Build the Docker image:
```bash
docker build -t mukamara-app .
```

3. Run the container:
```bash
docker run -p 8080:8080 mukamara-app
```

The app will be available at http://localhost:8080

## Deployment

This application is containerized and ready for deployment to any cloud platform that supports Docker containers.

### Environment Variables

- `PORT`: The port on which the server will run (default: 8080)

### Deployment Steps

1. Build the Flutter web app locally:
```bash
flutter build web
```

2. Build the Docker image:
```bash
docker build -t mukamara-app .
```

3. Tag the image for your container registry:
```bash
docker tag mukamara-app [registry-url]/mukamara-app
```

4. Push the image to your container registry:
```bash
docker push [registry-url]/mukamara-app
```

5. Deploy using your cloud platform's container deployment service.

## Cloud Platform Specific Instructions

### Google Cloud Run
```bash
gcloud run deploy mukamara --image [registry-url]/mukamara-app --platform managed
```

### Heroku
```bash
heroku container:push web
heroku container:release web
```

### AWS ECS
Deploy using the AWS ECS console or AWS CLI with your task definition.
