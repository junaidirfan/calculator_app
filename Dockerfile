# Use a lightweight Python image

FROM python:3.11-slim

# Set the working directory

WORKDIR /app

# Copy only necessary files first for layer caching

COPY requirements.txt .

# Install dependencies

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app

COPY . .

# Expose Flask port

EXPOSE 5000

# Run the Flask app as a non-root user

USER 1000

# Command to run the Flask app

CMD ["python", "app.py"]