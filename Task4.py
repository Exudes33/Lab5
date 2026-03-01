import re

s = input()
d = re.findall(r"\d", s)

print(" ".join(d))
