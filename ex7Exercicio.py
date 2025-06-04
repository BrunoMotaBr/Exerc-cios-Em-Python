nomes = []
cidades = set()
anos_nascimento = (1995, 2000, 1987)
i = 0

while(i < 3):
    i += 1
    nomes.append(input(f"Digite o {i}° nome: "))
    cidades.add(input(f"Digite a {i}ª cidade: "))

cadastro_pessoas = {"nomes": nomes,"anos": anos_nascimento,"cidades": cidades}

nomes.sort()

for nome in nomes:
    print(nome)
print(cidades)

print(f"{cadastro_pessoas["nomes"][1]} mora em {cidades}")

cidades.add("Curitiba")

for cidade in cidades:
    print(cidade)

for nome, ano in zip(cadastro_pessoas["nomes"], cadastro_pessoas["anos"]):
    print(nome)
    print(ano)


for cidade in cadastro_pessoas["cidades"]:
    print(cidade)