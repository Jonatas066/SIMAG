# SIMAG – Sistema de Alerta e Monitoramento de Gases

Sistema de monitoramento de qualidade do ar e detecção de gases tóxicos (incluindo gás de cozinha), com alertas em tempo real.

O projeto combina um sensor de gás (MQ-135) conectado a um ESP32 com um painel web desenvolvido em Flask, que exibe os dados em tempo real através do Firebase.

## Funcionalidades

- Monitoramento da qualidade do ar em tempo real
- Detecção de gases tóxicos / gás de cozinha
- Alerta sonoro via buzzer
- Painel web para visualização dos dados
- Comunicação entre ESP32 e Firebase

## Tecnologias Utilizadas

**Backend / Web**
- Python 3
- Flask
- Firebase Realtime Database

**Hardware**
- ESP32 DevKit V1
- Sensor MQ-135 (qualidade do ar / gases)
- Buzzer

## Como executar o projeto

### 1. Pré-requisitos
- Python 3.10 ou superior instalado
- Conta no Firebase

### 2. Clone o repositório
```bash
git clone https://github.com/Jonatas066/SIMAG.git
cd SIMAG

## Crie e ative o ambiente virtual 
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate

## Instale as depências
pip install -r requirements.txt
```

## Configure as credenciais do Firebase 

- Baixe o arquivo de credenciais do Firebase (service account)
- Não coloque o arquivo .json dentro do repositório
- Configure as variáveis de ambiente ou ajuste o caminho no código

## Execução da aplicação
```bash
python app.py
```
Acesse no navegador com o link que for fornecido no terminal

## Estrutura do Projeto
SIMAG/
├── app.py                      # Aplicação principal Flask
├── requirements.txt            # Dependências do projeto
├── .gitignore
├── README.md
├── static/                     # Arquivos estáticos
│   ├── imagens/
│   │   ├── g3.png
│   │   ├── logosimag.png
│   │   └── logosimag1.png
│   ├── styleindex.css
│   └── stylemonitoramento.css
└── templates/                  # Templates HTML
├── index.html
├── monitoramento.html
└── alerta.html