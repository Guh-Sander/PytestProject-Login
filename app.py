from userFuncion import*
from passwordFuncion import*
from messageFuncion import*
from cryptographyFramework import *

# Printa as regras de solicitação
def regras():
    rules = ('''Regras:
    O usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e com no máximo 30 caracteres.
    A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula e uma letra minúscula.
    A mensagem deve ter no máximo 70 caracteres.
    ''')
    return rules

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
    
# Chama as função para executar:
rules = print(regras())
user_end = valida_user()
print("Usuário válido!")
password_end = valida_password()
print("Senha válida!")
message_end = valida_msg()
print("Mensagem válida!")

# Escreve um arquivo ".txt":
initializeWrite()
# Encripta a mensagem e coloca ela em uma variável:
encrypt_message = encryptMessage(user_end, password_end, message_end)
# Salva a mensagem encriptada no arquivo ".txt":
saveNewLine(encrypt_message)