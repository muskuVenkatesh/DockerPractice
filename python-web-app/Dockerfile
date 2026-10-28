# Use official slim Python runtime (lightweight & secure)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Set default environment variables
ENV PORT=8080
ENV ENVIRONMENT=DockerPractice

# Copy application files into the container
COPY app.py .

# Inform Docker that the container listens on port 8080 at runtime
EXPOSE 8080

# Run the application when the container starts
CMD ["python", "app.py"]
