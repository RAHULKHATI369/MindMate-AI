# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all backend code into /app
COPY backend/ .

# Expose port 8080
EXPOSE 8080

# Run app with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
