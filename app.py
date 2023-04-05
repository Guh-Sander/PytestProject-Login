import re

# Printa as regras de solicitação
def regras():
    rules = ('''Regras:
    O usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e com no máximo 30 caracteres.
    A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula.
    A mensagem deve ter no máximo 70 caracteres.
    ''')
    return rules

# Solicita usuário
def loginUser_input():
    user = input(str("Digite seu usuário: "))
    return user

# Solicita senha
def loginPassword_input():
    password = input("Digite sua senha: ")
    return password

# Solicita mensagem para cryptografar:
def cryptMessage_input():
    msg = input("Digite a mensagem que deseja criptografar: ")
    return msg

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
    # Verifica se a senha possui menos que 10 caracteres.
    if len(password) < 10:
        return False
    else:
        return True

# Condições para o usuário:
def max_trinta_caracter(user):
    # Verifica se o nome do usuário possui mais de trinta caracteres.
    if len(user) > 30:
        return False
    else:
        return True

def ver_espaco(user):
    # Verifica se contêm algum espaço dentro do nome do usuário.
    if " " in user:
        return False
    else:
        return True

def ver_caracter(user):
    # Verifica se tem caracteres especiais.
    regex = re.compile('[^a-zA-Z0-9\s]')
    if regex.findall(user):
        return False
    else:
        return True

def ver_maiuscula(user):
    # Verifica se a primeira letra "user[0]" não é maiúscula pelo comando "isupper()" que mostra se é maiúscula ou não, assim printando que deve ser maiúscula.
    if not user[0].isupper():
        return False
    else:
        return True
    
# Condição da mensagem:
def ver_message(msg):
    # Verifica se a mensagem possui mais de 70 caracter.
    if len(msg) > 70:
        return False
    else:
        return True

# Valida condições do usuário:
def valida_user():
    while True:
        insereUser = loginUser_input()
        if ver_maiuscula(insereUser) and ver_caracter(insereUser) and ver_espaco(insereUser) and max_trinta_caracter(insereUser):
            break
        else:
            print("Usuário inválido! Deve começar com letra maiúscula, sem caracteres especiais e sem espaços, com no máximo 30 caracteres.\n")

# Valida condições da senha:
def valida_password():
    while True:
        inserePassword = loginPassword_input()
        if min_caracter(inserePassword) and caracter_senha(inserePassword) and ver_num(inserePassword) and letra_minu(inserePassword) and letra_mai(inserePassword):
            break
        else:
            print("Senha inválida! Deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula.\n")

# Valida condição da mensagem:
def valida_msg():
    while True:
        insereMsg = cryptMessage_input()
        if ver_message(insereMsg):
            break
        else:
            print("Mensagem inválida! Deve ter no máximo 70 caracteres.\n")
    
# Chama as função para exeutar:
rules = print(regras())
login = valida_user()
print("Usuário válido!")
password = valida_password()
print("Senha válida!")
msg = valida_msg()
print("Mensagem válida e criptografada com sucesso!")