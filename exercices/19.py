#Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar dois números iguais.

# Input dos numeros
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
# Faz a adição dos numeros
if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os números são iguais.")
    