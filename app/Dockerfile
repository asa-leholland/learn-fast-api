# Use the official Python image as the base image
FROM python:3.11-slim-buster AS base

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Develop image/stage
FROM base AS develop

# Set the working directory to /app
WORKDIR /app

# Copy the entire application to the container
COPY . .

# Set the environment variable for the development environment
ENV FASTAPI_ENV=development

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# Production image/stage
FROM base AS production

# Set the working directory to /app
WORKDIR /app

# Copy the entire application to the container
COPY . .

# Set the environment variable for the production environment
ENV FASTAPI_ENV=production

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
