# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the Python script to the container
COPY app.py .

# Run the Python script
CMD ["python", "app.py"]
