filmes_e_notas = list()
i = 0
total_notas = 0

while i < 3:
    i += 1
    filme = str(input("Digite o nome do filme: "))
    nota = float(input("Digite a nota do filme: "))
    filmes_e_notas.append({"filme": filme, "nota": nota})

for filme_e_nota in filmes_e_notas:
    print(f"Filme: {filme_e_nota["filme"].upper()} obteve a nota: {filme_e_nota["nota"]}")
    if(filme_e_nota["nota"] >= 7):
        print(f"{filme_e_nota["filme"]} obteve uma otima nota!!!")
    total_notas += filme_e_nota["nota"]

print(f"A média da nota de todos os filmes foi de {(total_notas / len(filmes_e_notas)):.2f}")

filmes_e_notas.sort(key=lambda item: item["nota"], reverse=True)
print(filmes_e_notas)