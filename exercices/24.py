##A partir de um vetor com 20 valores inteiros, o qual deve ser fornecido como entrada, verificar: (a) se todos os valores pertencem ao intervalo fechado [0,100] e, em caso afirmativo: (b) qual o valor mais frequente (moda).

# Input dos numeros
numeros = []
for i in range(20):
    numeros.append(int(input("Insira o número: ")))

# Verifica se todos os numeros estao no intervalo
for i in numeros:
    if i < 0 or i > 100:
        print("Nem todos os numeros estao no intervalo [0,100]")
        break
else:
    print("Todos os numeros estao no intervalo [0,100]")

    # Calcula a moda
    moda = max(set(numeros), key=numeros.count)
    print("A moda é:", moda)

    