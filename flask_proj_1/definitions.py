def generate_page(title:str, *products:list[str]|str, subtitle:str|None = None, components:list|None = None, disponibilita:dict|None = None):
  content = ''
  if len(products) > 1:
    for i, product in enumerate(products):
      for j, field in enumerate(product):
        if j != 3:
          content += f'<span>{str(field)} </span>'
      if i > 0:
        content += f'<i>&hearts;</i> <a style="text-decoration:none" href="/catalogo/{i}"> DETTAGLI </a><br><br><a style="text-decoration:none" href="/compra/{product[0]}"> COMPRA </a><br><br><p>DISP: {disponibilita[product[0]]}</p> <br><br>'
      else:
        content += '<br>'
  else:
    for product in products:
      content += f'<span>{str(product)} </span>'
      content += '<br>'

  print(content)
  return F"""<!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
  </head>
  <body>
    <header>
      <h1>{title}</h1>
      <h2>{subtitle}<h2>
    </header>
    <main>
      {content}
      {''.join(components) if components else ''}
    </main>
  </body>
  </html>"""


def render_component(name_file:str):
  with open(f'./components/{name_file}','r') as file:
    component = file.read()
    return component


