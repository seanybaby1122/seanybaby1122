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
# prompt: prompt: {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# {"from": "DATA", "to": "AGRA", "type": "Substitute"},
# {"from": "AGRA", "to": "EMIT", "type": "Substitute"},
# ],
# }
# .github/workflows/docker-ci.yml

# No preceding code is relevant to the task.
# Creating a dropdown menu with 3 random countries.
# The first option will be the default.

import random

# List of some countries
all_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
    "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
    "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
    "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
    "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo",
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"
]

# Get 3 random unique countries
random_countries = random.sample(all_countries, 3)

# Create the dropdown string for Colab forms
dropdown_string = '", "'.join(random_countries)
dropdown_string = f'"{dropdown_string}"'

# Create the Colab form variable
# The first item in the list will be the default
print(f'selected_country = "{random_countries[0]}" #@param [{dropdown_string}]')
# prompt: Define the file path
# file_path = os.path.join(directory, 'docker-ci.yml')
# Write the content to the file
# with open(file_path, 'w') as f: f.write(file_content)
# print(f"Created file: {file_path}")
# Optional: Verify the file creation
# !ls -l .github/workflows/
# prompt: prompt: {"from": "DATA", "to": "ATAD", "type": "Reverse"},
# {"from": "DATA", "to": "AGRA", "type": "Substitute"},

import os
directory = '.github/workflows'
if not os.path.exists(directory):
    os.makedirs(directory)
file_content = """name: Docker CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Log in to Docker Hub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKER_HUB_USERNAME }}
        password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v2
      with:
        context: .
        push: true
        tags: your_docker_hub_username/your_image_name:latest
"""

file_path = os.path.join(directory, 'docker-ci.yml')
with open(file_path, 'w') as f: f.write(file_content)
print(f"Created file: {file_path}")

# Optional: Verify the file creation
!ls -l .github/workflows/
# prompt: prompt: {"from": "DATA", "to": "ATAD", "type": "Reverse"},

def transform_string(prompt):
  """Transforms a string based on the given prompt.

  Args:
    prompt: A dictionary with 'from', 'to', and 'type' keys.

  Returns:
    The transformed string.
  """
  input_string = prompt["from"]
  transform_type = prompt["type"]

  if transform_type == "Reverse":
    return input_string[::-1]
  else:
    return "Unsupported transformation type"

# Example usage:
prompt = {"from": "DATA", "to": "ATAD", "type": "Reverse"}
transformed_string = transform_string(prompt)
transformed_string

