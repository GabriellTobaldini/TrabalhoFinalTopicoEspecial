# TrabalhoFinalTopicoEspecial - Gabriel Tobaldini

Projeto de Mineração de Dados com Python

Este projeto tem como objetivo aplicar conceitos de mineração de dados em um conjunto de dados utilizando Python e bibliotecas amplamente adotadas na comunidade de ciência de dados. O dataset escolhido é o Iris, que contém 150 registros e 5 colunas (4 atributos numéricos e a classe), ideal para exemplificar técnicas de classificação. O trabalho demonstra todo o processo, desde o carregamento dos dados até a geração de gráficos e métricas de avaliação de um modelo KNN (K-Nearest Neighbors).

Estrutura do Repositório
├── mineria.py           # Script principal com todo o código de análise
├── requirements.txt     # Lista de dependências do projeto
├── venv/                # Ambiente virtual (não versionado)
└── README.md            # Este arquivo de documentação

Tecnologias e Bibliotecas Utilizadas
Python 3.8

pandas
scikit-learn
matplotlib
seaborn

Passo a Passo para Reproduzir a Análise

Clonar o repositório
  git clone https://github.com/GabriellTobaldini/TrabalhoFinalTopicoEspecial.git

Após clonar, entre na pasta do repositório
  cd topicosespeciaiscomputacao

Criar e ativar o ambiente virtual
  python -m venv venv
  venv\Scripts\activate.bat

Instalar as dependências
  pip install -r requirements.txt

Executar o script de mineração
  python mineria.py

Ao rodar, serão exibidos no console:
  As primeiras cinco linhas do dataset
  A matriz de confusão
  O relatório de classificação
  Em seguida, serão abertas duas janelas de gráfico:
  Pairplot dos atributos do Iris
  Heatmap da matriz de confusão

Encerrar o ambiente virtual
  deactivate