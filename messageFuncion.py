# Solicita mensagem para cryptografar:
def cryptMessage_input():
    msg = input("Digite a mensagem que deseja criptografar: ")
    return msg
    
# Condição da mensagem:
def ver_message(msg):
    # Verifica se a mensagem possui mais de 70 caracter.
    if len(msg) > 70:
        return False
    else:
        return True