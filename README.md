# Busca de Dados de Ações da Apple

![Licença](https://img.shields.io/github/license/seu-usuario/busca_dados_acoes_apple)

## Descrição

Este é um exemplo simples de como utilizar a API 'yfinance' do Yahoo para buscar dados das ações da Apple Inc. na Bolsa de Valores dos EUA. O TICKER 'AAPL' é o símbolo usado para identificar as ações da empresa. É um código alfanumérico único atribuído a cada empresa com ações negociadas, amplamente usado para acompanhar e identificar as ações da empresa em diferentes plataformas financeiras e notícias relacionadas ao mercado de ações.

## Pré-requisitos

- Python 3.x
- Biblioteca 'yfinance'

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema. Caso ainda não tenha, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale a biblioteca 'yfinance' executando o seguinte comando no terminal ou prompt de comando:

```bash
pip install yfinance
```

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/busca_dados_acoes_apple.git
```

2. Navegue até o diretório do projeto:

```bash
cd busca_dados_acoes_apple
```

3. Execute o script Python para buscar os dados das ações da Apple:

```bash
python busca_dados_acoes_apple.py
```

4. O programa irá buscar os dados da ação da Apple (AAPL) entre as datas especificadas no código (DATA_INICIO e DATA_FIM) e calcular o ganho. O resultado será exibido no terminal.

## Personalização

Você pode personalizar os seguintes parâmetros no código 'busca_dados_acoes_apple.py':

- `TICKER`: Altere este valor para o TICKER da ação que deseja buscar os dados.
- `DATA_INICIO`: Defina a data de início para buscar os dados das ações.
- `DATA_FIM`: Defina a data de fim para buscar os dados das ações.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---

Criado por Marcos Silva.