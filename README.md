## prompt: {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
# ],
# }
# .github/workflows/docker-ci.yml

import os

# Create a directory structure that matches the path
directory = '.github/workflows/'
os.makedirs(directory, exist_ok=True)

# Define the content of the file
file_content = """
name: Docker CI

on: [push]

jobs:
  build_and_push:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Build Docker image
      run: docker build -t my-docker-image .

    - name: Log in to Docker Hub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKER_HUB_USERNAME }}
        password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

    - name: Push Docker image
      run: docker push my-docker-image
"""

# Define the file path
file_path = os.path.join(directory, 'docker-ci.yml')

# Write the content to the file
with open(file_path, 'w') as f:
  f.write(file_content)

print(f"Created file: {file_path}")

# Optional: Verify the file creation
!ls -l .github/workflows/

