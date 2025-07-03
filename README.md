seanybaby1122.github.io
prompt: # Method 1: Make a request to the website (to check if it's accessible or get content)
import requests
try:
response = requests.get("https://seanybaby1122.github.io")
if response.status_code == 200:
print("Website is accessible. Status code:", response.status_code)
# You can optionally print the content
# print(response.text)
else:
print(f"Failed to access website. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
print(f"An error occurred while accessing the website: {e}")
# prompt: Method 2: Display the website in an iframe (might not work reliably due to security restrictions)
from IPython.display import HTML
# Replace 'https://www.example.com' with the URL you want to display
url = 'https://www.example.com'
# Use an iframe to embed the website
display(HTML(f'<iframe src="{url}" width="800" height="600"></iframe>'))
from IPython.display import HTML
# Replace 'https://www.example.com' with the URL you want to display
url = 'https://www.example.com'
# Use an iframe to embed the website
display(HTML(f'<iframe src="{url}" width="800" height="600"></iframe>'))
from IPython.display import HTML
# Replace 'https://www.example.com' with the URL you want to display
url = 'https://www.example.com'
# Use an iframe to embed the website
display(HTML(f'<iframe src="{url}" width="800" height="600"></iframe>'))
from IPython.display import HTML
# Replace 'https://www.example.com' with the URL you want to display
url = 'https://www.example.com'
# Use an iframe to embed the website
display(HTML(f'<iframe src="{url}" width="800" height="600"></iframe>'))
# from IPython.display import IFrame
# IFrame("https://seanybaby1122.github.io", width=800, height=600)
# Method 3: Open the link in a new browser tab (user action required)
# from IPython.display import display, HTML
# display(HTML('Open seanybaby1122.github.io'))
The previous code snippet attempts to display a website in an iframe,
but this is often blocked by modern browsers due to security policies (like X-Frame-Options).
It also repeats the same iframe code multiple times unnecessarily.
A more reliable way to view a website is to simply provide a clickable link to open it in a new tab
