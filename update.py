#!python
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

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
      <form action="process_update.py" method="post">
          <input type="hidden" name="pageId" value="{form_title}">
          <p><input type="text" placeholder="title" name="title" value="{form_title}"></P>
          <p><textarea rows="4" name="description">{form_description}</textarea></P>
          <p><input type="submit" value="submit"></p>
      </form>
      <h2>{title}</h2>
      <p>{desc}</p>
    </body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_title=pageId, form_description=description))
