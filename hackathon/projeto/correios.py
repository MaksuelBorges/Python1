import requests

def obter_informacoes_cep():
    cep = input('Digite seu CEP: ')

    cep = cep.replace('-', '').replace(',', '').replace(' ', '')

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(link)

        print(requisicao)

        dic_requisicao = (requisicao.json())
        uf = dic_requisicao['uf']
        ddd = dic_requisicao['ddd']
        cidade = dic_requisicao['localidade']
        bairro = dic_requisicao['bairro']
        logradouro = dic_requisicao['logradouro']
        print(f'Estado: {uf}\nDDD: {ddd}\nCidade: {cidade}\nBairro: {bairro}\nRua: {logradouro}')

    else:
        print('CEP Inválido')
    return '', '', '', '', ''
correios = obter_informacoes_cep()
