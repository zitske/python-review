##Dado valor em dólares, e uma cotação, converter para reais (R$).

# Input do valor em dólares
dolar = float(input("Insira o valor em dólares: "))
# Input da cotação
cotacao = float(input("Insira a cotação do dólar: "))
# Faz a conversão
real = dolar * cotacao
# Mostra o resultado
print("O valor em reais é:", real)