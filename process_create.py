#!python
import cgi, os
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

with open("data/"+title, 'w+t', encoding="utf-8") as fp:
    fp.write(description)

print("Location: index.py?id="+title)
print()
