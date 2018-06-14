#!python
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

with open("data/"+pageId, 'w+t', encoding="utf-8") as fp:
    fp.write(description)

os.rename("data/"+pageId,"data/"+title)
print("Location: index.py?id="+title)
print()
