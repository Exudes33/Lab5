import re

s = input()
m = re.findall(r"\b\w{3}\b", s)

print(len(m))
