

import re

mathcher = re.finditer("\w*", "rahul Gandhi")

for match in mathcher:
    print(match.start(), match.group())
