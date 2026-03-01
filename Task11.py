import re

s = input()
m = re.findall(r"[A-Z]", s)

print(len(m))
