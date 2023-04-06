import re
# Solicita senha
def loginPassword_input():
    password = input("Digite sua senha: ")
    return password

# Condições para a senha:
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
        return False
    else:
        return True

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
        return False
    else:
        return True

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
        return False
    else:
        return True

def caracter_senha(password):
    # Verifica se a senha não possui caracteres especiais.
    regex = re.compile('[^a-zA-Z0-9\s]')
    if not regex.findall(password):
        return False
    else:
        return True

def min_caracter(password):
    # Verifica se a senha possui menos 10 caracteres.
    if len(password) < 10:
        return False
    else:
        return True