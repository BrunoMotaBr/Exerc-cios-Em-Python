produtos = []
precos = (19.90, 5.50, 13.75)
categorias = {"Alimento", "Limpeza", "Eletrônico", "Alimento"}

i = 0
while(i < 3):
    i +=1
    produtos.append(input(f"Digite o {i}° produto:"))

estoque = {"Produtos": produtos,"Precos": precos, "Categorias": categorias}

produtos.sort()

print(produtos)
print(estoque["Precos"][2])
categorias.add("Higiene")
print(categorias)

for produto, preco in zip(estoque["Produtos"], estoque["Precos"]):
    print(f"Produto: {produto} R${preco}")

for categoria in estoque["Categorias"]:
    print(f"Categoria: {categoria}")