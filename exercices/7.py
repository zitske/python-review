##Encontrar a soma dos números inteiros a partir de 1 até N, com incrementos de 3 em 3. Exemplo: 1+4+7+10+13+16+19, para N=19.

# Input do numero
num = int(input("Insira o número: "))
# Cria a lista
my_list = []
# Cria o contador
i = 1
# Loop
while i <= num:
    # Adiciona o numero na lista
    my_list.append(i)
    # Incrementa o contador
    i += 3
# Mostra a lista
print(my_list)
# Soma os valores da lista
result = sum(my_list)
# Mostra o resultado
print("A soma dos números inteiros a partir de 1 até", num, "com incrementos de 3 em 3 é:", result)