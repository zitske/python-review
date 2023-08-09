##Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:
#"O número [número] é [par/ímpar]"

# Input dos numeros
num = int(input("Insira um número: "))
# Faz a adição dos numeros
if num % 2 == 0:
    result = "par"
else:
    result = "ímpar"
# Mostra o resultado
print("O número", num, "é", result)
