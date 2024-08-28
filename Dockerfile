# Use an official Python runtime as a parent image
FROM python:3.11

RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script.py when the container launches
CMD ["python3", "script.py"]
