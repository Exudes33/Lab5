import re

s = input()
res = re.sub(r"\d", lambda x: x.group(0) * 2, s)

print(res)
