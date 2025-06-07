import requests
import re

url = "http://challenges.ringzer0team.com:10032"

response = requests.get(url)
content = response.text

# Lọc bỏ thẻ HTML
clean_text = re.sub(r'<.*?>', '', content)

# Trích xuất biểu thức
match = re.search(r"----- BEGIN MESSAGE -----\s*(.*?)\s*----- END MESSAGE ----", clean_text, re.DOTALL)
expr = match.group(1).strip()

# Loại bỏ '= ?'
expr = expr.replace("= ?", "").strip()

def convert_number(token):
    token = token.strip()
    if token.startswith("0x") or token.startswith("0X"):
        return str(int(token, 16))
    elif all(c in "01" for c in token) and len(token) > 8:
        return str(int(token, 2))
    else:
        return token

tokens = expr.split()
tokens_converted = [convert_number(t) if not t in ['+', '-', '*', '/', '(', ')'] else t for t in tokens]
expr_converted = " ".join(tokens_converted)

result = eval(expr_converted)



# Gửi lại kết quả
answer_url = f"{url}/?r={result}"
answer = requests.get(answer_url).text
flag_match = re.search(r"FLAG-\w+", answer)
if flag_match:
    print("FLAG found:", flag_match.group(0))
else:
    print("No flag found. Full response:")
    print(answer)
