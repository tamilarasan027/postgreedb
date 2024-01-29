# Use an official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=joosika
ENV POSTGRES_USER=marriage
ENV POSTGRES_PASSWORD=joosika

# Copy the SQL schema file into the container
COPY schema.sql /docker-entrypoint-initdb.d/

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY script.py .

# Install the required Python packages
RUN pip3 install psycopg2-binary

# Run the Python script when the container starts
CMD ["python3", "script.py"]
