#Crie um módulo chamado `data` com uma função que recebe uma data no formato
#"dd/mm/aaaa" e verifica se é válida.

def data_valida(data):
    try:
        from datetime import datetime
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False
