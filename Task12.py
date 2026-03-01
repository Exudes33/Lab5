import re

s = input()
m = re.findall(r"\d{2,}", s)

print(" ".join(m))
