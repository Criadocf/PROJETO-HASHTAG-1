# abrir os 6 arquivos

# para cada arquivo:

# verificar se algum valor da coluna Vendas é igual ou maior que 55.000

# Se sim, enviar SMS com o mês e as vendas do vendedor.

import pandas as pd #pandas FAZ A INTERAÇÃO DO PYTHON COM O EXCEL.

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in meses:
    tabelas = pd.read_excel(f'{mes}.xlsx') #VARIÁVEL USADA PARA ARMAZENAR A LEITURA DAS TABELAS..
    print(mes)
    print(tabelas)
    if (tabelas['Vendas'] >= 55.000).any(): #any SIGNIFICA ALGUM, "SE ALGUM VALOR DA TABELA Vendas for maior que 55.000, então envie um SMS"
        print(f'No mês de {mes} encontrou alguém que vendeu mais de  55 mil')
        
    



