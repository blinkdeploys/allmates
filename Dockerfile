# Use the official Python image.
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and ensure logs are displayed in the terminal.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Copy requirements.txt and install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /usr/src/app/

# Expose the port the app will run on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
