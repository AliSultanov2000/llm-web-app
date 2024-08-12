# Use base image
FROM python:3.10

# Install work directory
WORKDIR /mysite

# Copy requirements.txt 
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the code of app in docker container
COPY . .

# Run command to start docker app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]