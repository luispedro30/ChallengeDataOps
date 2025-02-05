FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entire content of the current directory (on your local machine) to the container's /app directory
COPY . .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for Flask/Dash application
EXPOSE 5000

# Set the command to run the application using the correct file (src/dashboard.py)
CMD ["python", "src/dashboards.py"]
