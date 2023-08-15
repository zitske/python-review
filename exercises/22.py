##A partir de um valor dado em segundos, calcular o valor correspondente em horas, minutos e segundos. 

# Input dos segundos
segundos = int(input("Insira o valor em segundos: "))
# Calcula as horas
horas = segundos // 3600
# Calcula os minutos
minutos = (segundos % 3600) // 60
# Calcula os segundos
segundos = (segundos % 3600) % 60
# Mostra o resultado
print("O resultado é:", horas, "horas,", minutos, "minutos e", segundos, "segundos.")