import re

# solicita usuário
def loginUser_input():
    print('''Regras:
    O usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e com no máximo 30 caracteres.
    A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula.
    ''')
    user = input(str("Digite seu usuário: "))

# Solicita senha
def loginPassword_input():
    password = input("Digite sua senha: ")

# Condições para o usuário e senha
def letra_mai(password):
    # Verifica se na senha pelo menos uma letra maiúscula.
    letra_maiuscula = False
    # Passa caracter por caracter verificando se a senha possui um caracter maiúsculo e se tiver, define "True" e para a verificação pelo "break".
    for caracter in password:
        if caracter.isupper():
            letra_maiuscula = True
            break  
    # Logo abaixo, o código mostra que se não for "True", print que deve ter uma letra maiúscula, se não apenas passa para o próximo comando.
    if not letra_maiuscula:
        print("A senha deve conter pelo menos uma letra maiúscula.")
    else:
        pass

def letra_minu(password):
    # Verifica se na senha pelo menos uma letra minúscula.
    letra_minuscula = False
    # Passa caracter por caracter verificando se a senha possui um caracter minúsculo e se tiver, define "True" e para a verificação pelo "break".
    for caracter in password:
        if caracter.islower():
            letra_minuscula = True
            break
    # Logo abaixo, o código mostra que se não for "True", print que deve ter uma letra minúscula, se não apenas passa para o próximo comando.
    if not letra_minuscula:
        print("A senha deve conter pelo menos uma letra minuscúla.")
    else:
        pass

def ver_num(password):
    # Verifica se a senha possui pelo menos algum número.
    possui_num = False
    # Passa caracter por caracter verificando se a senha possui número, se tiver número define "True" e para a verificação.
    for caracter in password:
        if caracter.isdigit():
            possui_num = True
            break
    # Logo abaixo, o código mostra que se não for "True", print que deve ter números, se não apenas passa para o próximo comando.
    if not possui_num:
        print("A senha deve ter pelo menos um número.")
    else:
        pass

def caracter_senha(password):
    # Verifica se a senha não possui caracteres especiais.
    regex = re.compile('[^a-zA-Z0-9\s]')
    if not regex.findall(password):
        print("A senha deve conter pelos menos um caracter especial.")
    else:
        pass

def min_caracter(password):
    # Verifica se a senha possui menos que 10 caracteres.
    if len(password) < 10:
        print("A senha deve ter no minimo 10 caracteres.")
    else:
        pass

def max_trinta_caracter(user):
    # Verifica se o nome do usuário possui mais de trinta caracteres.
    if len(user) > 30:
        print("Deve conter no máximo 30 carácter.")
    else:
        pass

def ver_espaco(user):
    # Verifica se contêm algum espaçamento no nome do usuário, passando letra por letra vendo se alguma delas é espaço.
    for letras in user:
        if letras.isspace():
            print("Não deve conter espaçamento.")
        else:
            pass

def ver_caracter(user):
    # Verifica se tem caracteres especiais.
    regex = re.compile('[^a-zA-Z0-9\s]')
    if regex.findall(user):
        print("Não deve conter caracteres especiais no usuário.")
    else:
        pass

def ver_maiuscula(user):
    # Verifica se a primeira letra "user[0]" não é maiúscula pelo comando "isupper()" que mostra se é maiúscula ou não, assim printando que deve ser maiúscula.
    if not user[0].isupper():
        print("A primeira letra deve ser maiúscula.")
    else:
        return True

# Valida condições:
def valida():
    # Insere o usuário e senha
    insereUser = loginUser_input()
    inserePassword = loginPassword_input()
    # condição do usuário

    # condição da senha 
    cond1_password = letra_mai(inserePassword)
    print(cond1_password)
valida()
