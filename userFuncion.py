import re
# Solicita usuário
def loginUser_input():
    user = input(str("Digite seu usuário: "))
    return user

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