# Use an official Python runtime as a parent image
FROM python:3.11.1-slim

# Set the working directory inside the container
WORKDIR /vidalgorithm

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]
