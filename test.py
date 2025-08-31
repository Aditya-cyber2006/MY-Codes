import requests

# Your prompt
prompt = "who invented python "
prompt=prompt+" give short response"

# Encode the prompt for a URL
encoded_prompt = prompt.replace(" ", "%20")

# Create the URL
url = f"https://text.pollinations.ai/{encoded_prompt}"

# Make the GET request
response = requests.get(url)

# Get the response text
if response.status_code == 200:
    print("AI Response:\n", response.text)
else:
    print("Error:", response.status_code)
