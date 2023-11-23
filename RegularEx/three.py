import re

matcher = re.finditer("[^a-zA-Z0-9]", "91+9591619191")

for match in matcher:
    print(match.start(), match.group())
