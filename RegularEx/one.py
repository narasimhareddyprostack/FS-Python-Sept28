import re
st = input("Enter Data:")  # uiuy

matcher = re.finditer("[^abcd]", st)

for match in matcher:
    print(match.start(), match.group())
