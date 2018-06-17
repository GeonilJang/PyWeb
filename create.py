#!python
print("Content-Type: text/html")
print()
import cgi, os
from module import getList


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

print('''
<!doctype html>
    <html>
    <head>
      <title>PyWeb</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="index.py">WEB</a></h1>
      <ol>
        {listStr}
      </ol>
      <a href="create.py">create<a>
      <form action="process_create.py" method="post">
          <p><input type="text" placeholder="title" name="title"></P>
          <p><textarea rows="4" name="description"></textarea></P>
          <p><input type="submit" value="submit"></p>
      </form>
      <h2>{title}</h2>
      <p>{desc}</p>
    </body>
</html>
'''.format(title=pageId, desc=description, listStr=getList()))
