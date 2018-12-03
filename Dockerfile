FROM python:3.6

# Set the working directory to /project
WORKDIR /project

# Copy the current directory contents into the container at /project
ADD . /project

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run test_gmail.py when the container launches
CMD ["pytest", "tests/test_gmail.py"]
