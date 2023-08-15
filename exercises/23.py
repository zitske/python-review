## Dado o dia de nascimento de uma pessoa, calcular o número total de dias vividos até a data de hoje.

# Importa o pacote datetime
import datetime

# Input da data de nascimento
data = input("Insira a data de nascimento (dd/mm/aaaa): ")

# Converte a data para o formato datetime
data = datetime.datetime.strptime(data, "%d/%m/%Y")

# Calcula a diferença entre a data de hoje e a data de nascimento
diferenca = datetime.datetime.now() - data

# Mostra a diferença em dias
print("Você viveu", diferenca.days, "dias até hoje.")