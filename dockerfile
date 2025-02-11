# Step 1: Use an official Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the script from local machine to the container
COPY fetchCommit.py /app/fetch_commits.py

# Step 4: Install required dependencies
RUN pip install requests

# Step 5: Define default environment variables
ENV REPO_OWNER="microsoft"
ENV REPO_NAME="playwright"

# Step 6: Command to run the script
CMD ["python", "/app/fetch_commits.py"]

