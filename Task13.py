import re

s = input()
m = re.findall(r"\w+", s)

print(len(m))
