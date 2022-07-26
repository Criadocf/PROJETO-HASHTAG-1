# abrir os 6 arquivos

# para cada arquivo:

# verificar se algum valor da coluna Vendas é igual ou maior que 55.000

# Se sim, enviar SMS com o mês e as vendas do vendedor.

#USO O pip install 'biblioteca' PARA IMPORTAR ALGO(TERMINAL).

import openpyxl

import pandas as pd #pandas FAZ A INTERAÇÃO DO PYTHON COM O EXCEL.

from twilio.rest import Client #twilio.rest FAZ A INTERAÇÃO COM O ENVIO DE SMS.

account_sid = "AC22fb2e409e0e51e256ee5062f3951ec4"
# Your Auth Token from twilio.com/console
auth_token  = "7f305a8145c6d86f38ee7124051c7010"

client = Client(account_sid, auth_token)

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in meses:
    tabelas = pd.read_excel(f'{mes}.xlsx') #VARIÁVEL USADA PARA ARMAZENAR A LEITURA #DAS TABELAS..#
    if (tabelas['Vendas'] > 55000).any():
        vendedor = tabelas.loc[tabelas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelas.loc[tabelas['Vendas'] > 55000, 'Vendas'].values[0] #.loc USO PRA ACHAR O CONTEUDO QUE EXISTE EM UMA LINHA, RECEBE DOIS PARÂMETROS ENTRE COLCHETES. UMA CONDIÇÃO E O NOME DA COLUNA. DESSA FORMA ELE ME RETORNARIA UMA TABELA, COISA Q NAO QUERO, ENTÃO USO O values[0], DESSA FORMA ME RETORNA O ELEMENTO DA CÉLULA.
        print(f'No mês de {mes}, o vendedor {vendedor} vendeu mais de R$55000, Pra ser mais preciso, a venda foi de R${vendas}')
        message = client.messages.create(
        to="+5586994924740", 
        from_="+13256665061",
        body=f'No mês de {mes}, o vendedor {vendedor} vendeu mais de R$55000, Pra ser mais preciso, a venda foi de R${vendas}')
        print(message.sid)





    
        
    



