##Escreva um programa que receba dois números e um operador (+,-,* ou /) , e faça a operação matemática definida pelo sinal.

# Input dos numeros
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
op = input("Insira o operador: ")

# Faz a adição dos numeros
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Operador inválido")
    exit()

# Mostra o resultado
print("O resultado da operação de", num1, op, num2, "é:", result)