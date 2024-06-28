FROM python:3.12-slim-bullseye

WORKDIR /app

# Install only the necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the deploy script
RUN python deploy.py

WORKDIR /app/backend

# Expose the application port
EXPOSE 8000

# Set the environment variable
ENV NAME World

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
