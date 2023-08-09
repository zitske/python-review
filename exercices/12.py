##Faça um programa que leia uma senha, até que a senha esteja correta.

# Input da senha
senha = input("Insira a senha: ")

# Enquanto a senha estiver errada
while senha != "senhacorreta":
    # Input da senha
    senha = input("Insira a senha: ")

# Mostra a senha
print("A senha está correta!")
