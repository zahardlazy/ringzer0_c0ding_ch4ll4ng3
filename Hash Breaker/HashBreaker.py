import requests
import re
import hashlib

URL = "http://challenges.ringzer0team.com:10056"
# Get the challenge page
r = requests.get(URL)

# Extract the hash from the page
match = re.search(r"----- BEGIN HASH -----(.*?)----- END HASH -----", r.text, re.DOTALL)
if not match:
    print("Hash not found!")
    exit(1)
target_hash = match.group(1).replace("<br />", "").strip()
print("Target hash:", target_hash)

# Brute-force the original value (assuming it's a number between 0 and 99999)
answer = None
for i in range(100000):
    s = str(i)
    if hashlib.sha1(s.encode()).hexdigest() == target_hash:
        answer = s
        break

if answer is None:
    print("No matching value found!")
    exit(1)

# Send the answer back
response = requests.get(f"{URL}/?r={answer}")
print(response.text)
