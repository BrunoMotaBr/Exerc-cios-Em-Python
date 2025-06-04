livro = {"titulo": "Chapeuzinho vermelho","autor": "Frank Husvel", "ano": 1935}
biblioteca = [livro]
livro2 = {"titulo": "O magico de Oz","autor": "Bruno Mota", "ano": 2005}
biblioteca.append(livro2)

for liv in biblioteca:
    print(liv["titulo"])
