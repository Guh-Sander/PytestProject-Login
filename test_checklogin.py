from userFuncion import*
from passwordFuncion import*
from messageFuncion import*

def teste_user():
    # Testa se o nome do usuário não tem mais de trinta caracteres.
    assert True == max_trinta_caracter("Gustavo")
    assert False == max_trinta_caracter("GustavoGustavoGustavoGustavoGustavoGustavoGustavoGustavoGustavoGustavoGustavoGustavo")
    # Testa se não contêm algum espaço dentro do nome do usuário.
    assert True == ver_espaco("Gustavo")
    assert False == ver_espaco("Gustavo Henrique Sander")
    # Testa se não tem caracteres especiais.
    assert True == ver_caracter("Gustavo")
    assert False == ver_caracter("@Gustavo")
    # Testa se a primeira letra não é maiúscula.
    assert True == ver_maiuscula("Gustavo")
    assert False == ver_maiuscula("gustavo")

def teste_password():
    # Testa se na senha pelo menos uma letra maiúscula.
    assert True == letra_mai("@Gustavo16")
    assert False == letra_mai("@gustavo16")
    # Testa se tem pelo menos uma letra minúscula.
    assert True == letra_minu("@Gustavo16")
    assert False == letra_minu("@GUSTAVO16")
    # Testa se a senha possui pelo menos algum número.
    assert True == ver_num("@Gustavo16")
    assert False == ver_num("@Gustavo")
    # Testa se a senha possui caracteres especiais.
    assert True == caracter_senha("@Gustavo16")
    assert False == caracter_senha("Gustavo16")
    # Testa se a senha possui menos 10 caracteres.
    assert True == min_caracter("@Gustavo16")
    assert False == min_caracter("@Gu16")

def testa_message():
    # Testa se a mensagem não possui mais de 70 caracter.
    assert True == ver_message("Hum, zé da manga.")
    assert False == ver_message("Hum, zé da manga. Hum, zé da manga. Hum, zé da manga. Hum, zé da manga. Hum, zé da manga. Hum, zé da manga. Hum, zé da manga.")