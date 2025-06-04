frase = "  Estudar Python é divertido e produtivo.  "
contador = 0

print(frase.upper())
for letra in frase:
    if letra.lower() == "o":
        contador += 1
print(contador)
print(frase.split())
print(frase.replace("divertido", "incrível"))
print(frase.strip())