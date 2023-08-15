##Mostrar na tela a lista dos primeiros 1000 números primos.

# Funcao para seber se é primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Lista de primos
i = 0;
primos = []

# Loop para achar os primos
while len(primos) < 1000:
    if is_prime(i):
        primos.append(i)
    i += 1

# Mostra os primos
print(primos)