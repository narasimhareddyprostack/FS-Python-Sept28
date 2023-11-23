import re

matcher = re.finditer("[\S]", "rahul gandhi Wayanad")
#                              012345

for match in matcher:
    print(match.start(), match.group())
