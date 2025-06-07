import requests
import re
import hashlib

url = "http://challenges.ringzer0ctf.com:10013"

# Step 1: Get the page
response = requests.get(url)
content = response.text

# Step 2: Extract the message
match = re.search(r"----- BEGIN MESSAGE -----(.*?)----- END MESSAGE -----", content, re.DOTALL)
message = match.group(1).replace("<br />", "").strip()

# Step 3: Hash the message
hashed = hashlib.sha512(message.encode()).hexdigest()

# Step 4: Submit the response
answer_url = f"{url}/?r={hashed}"
answer = requests.get(answer_url).text

# Step 5: Extract the flag from response
flag_match = re.search(r"FLAG-\w+", answer)
if flag_match:
    print("FLAG found:", flag_match.group(0))
else:
    print("No flag found. Full response:")
    print(answer)
