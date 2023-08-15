##Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

# Input das notas
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
# Faz a adição dos numeros
media = (nota1 + nota2)/2
# Mostra o resultado
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

