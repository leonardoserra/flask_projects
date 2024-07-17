def generate_page(title:str, *html_tag:list[str], subtitle:str|None = None):
  content = ''
  if len(html_tag)>1:
    for element in html_tag:
      for field in element:
        content += f'<span>{str(field)} </span>'
      content += '<br>'
  else:
    for element in html_tag:
      content += f'<span>{str(element)} </span>'
      content += '<br>'

  return F"""<!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
  </head>
  <body>
    <header>
      <h1>Buongiorno, sono {title}</h1>
      <h2>{subtitle}<h2>
    </header>
    <main>
      {content}
    </main>
  </body>
  </html>"""