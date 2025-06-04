nomes = ["Bruno", "Carlos", "Ana", "Bruno"]
idades = (25, 30, 22)
cidades = {"São Paulo", "Rio de Janeiro", "São Paulo"}

cadastro = {"nomes": nomes,
            "idades": idades,
            "cidades": cidades}

# Remover nomes repetidos
nomes_nao_repetidos = list(set(nomes))
cadastro["nomes"] = nomes_nao_repetidos
print(nomes_nao_repetidos)

# Idade da segunda pessoa
print(idades[1])

# Mostrar cidades
print(cidades)
cidades.add("Curitiba")
print(cidades)

# Mostrar nomes e idades juntos (se possível)
for nome, idade in zip(cadastro["nomes"], cadastro["idades"]):
    print(f"Nome: {nome}, Idade: {idade}")

# Mostrar todas as cidades
for cidade in cadastro["cidades"]:
    print(f"Cidade: {cidade}")
