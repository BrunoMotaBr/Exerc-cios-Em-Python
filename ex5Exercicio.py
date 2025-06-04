nomes = ["Bruno", "Carlos", "Ana", "Bruno"]
idades = (25, 30, 22)
cidades = {"São Paulo", "Rio de Janeiro", "São Paulo"}


cadastro = {"nomes": nomes,
            "idades": idades,
            "cidades": cidades}

nomes_nao_repetidos = []

for n in nomes:
    if(n in nomes_nao_repetidos):
        pass
    else:
        nomes_nao_repetidos.append(n)
        print(n)

cadastro["nomes"] = nomes_nao_repetidos

print(idades[1])
print(cidades)
cidades.add("Curitiba")
print(cidades)


for primeira_variavel, segunda_variavel, terceira_variavel in cadastro["nomes"],cadastro["idades"], cadastro["cidades"]:
    print(f"Primeira variavel: {primeira_variavel}; Segunda variavel: {segunda_variavel}; Terceira variavel: {terceira_variavel}")
    