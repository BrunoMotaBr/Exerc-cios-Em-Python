texto = "  Olá, Bruno! Bem-vindo ao Python.  "

print(texto.lower())     # tudo minúsculo
print(texto.upper())     # tudo maiúsculo
print(texto.strip())     # remove espaços no início e fim
print(texto.replace("Bruno", "Carlos"))  # substitui
print(texto.split(" "))  # separa a string em lista por espaço
print(len(texto))        # tamanho da string (quantidade de caracteres)
print(texto.find("Python"))  # posição onde começa a palavra "Python"
print(texto.count("o"))  # conta quantas vezes aparece o caractere "o"
print(texto.startswith("Olá"))  # verifica se começa com "Olá"
print(texto.endswith("."))      # verifica se termina com "."