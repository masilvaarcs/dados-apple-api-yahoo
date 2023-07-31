"""
Montei esse exemplo de como poderia ser acessado a API 'yfinance' do Yahoo para buscar dados das
ações. TICKER ='AAPL' é o símbolo usado para identificar as ações da Apple Inc. na Bolsa de
Valores dos EUA. É um código alfanumérico único atribuído a cada empresa com ações negociadas,
amplamente usado para acompanhar e identificar as ações da empresa em diferentes plataformas
financeiras e notícias relacionadas ao mercado de ações.
"""

import yfinance as yf


# Função para obter os dados da ação através da API yfinance
def obter_dados_acao(ticker: str, data_inicio: str, data_fim: str):
    acao = yf.download(ticker, data_inicio, data_fim)
    return acao


# Função para calcular o ganho com base nos dados obtidos
def calcular_ganho(dados_acao):
    preco_compra = dados_acao['Close'].iloc[0]
    preco_venda = dados_acao['Close'].iloc[-1]
    ganho = preco_venda - preco_compra
    return ganho


if __name__ == "__main__":
    # Dados da Apple (faça os ajustes desejados)
    TICKER = 'AAPL'
    DATA_INICIO = '2022-01-01'
    DATA_FIM = '2023-01-01'

    # Buscar os dados da ação
    dados_apple = obter_dados_acao(TICKER, DATA_INICIO, DATA_FIM)

    print(dados_apple.head())

    # Chama a função para calcular o ganho
    ganho_ou_perda = calcular_ganho(dados_apple)

    # Mostrar se Ganhou ou Perdeu dinheiro
    if ganho_ou_perda < 0:
        STR_PERDA_GANHO = ' PERDEU '
    else:
        STR_PERDA_GANHO = ' GANHOU '

    msg = f'Você{STR_PERDA_GANHO}US${ganho_ou_perda:,.2f} por ação.'
    print(msg)
