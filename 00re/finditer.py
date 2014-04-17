#!/usr/bin/env python
import re,sys
if __name__=="__main__":
    text="""<html>
<body>
hello
test
</body>
</html>
"""
    for m in re.finditer(r"(?P<emelemet><[\w\s]+>|</[\w\s]+>)", text):
        print m.groupdict()
