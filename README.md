# LLMlocal
 Suporte ao Cliente LLM com Interface Gráfica (GUI)
 Este repositório fornece uma interface gráfica (GUI) para interagir com um modelo de linguagem grande (LLM) e obter respostas para perguntas em um contexto específico. A GUI facilita a formulação de perguntas e a visualização das respostas geradas pelo LLM.

Funcionalidades:
Carregar pasta de arquivos de contexto: Selecione uma pasta contendo arquivos de texto que serão utilizados como base para as respostas do LLM.
Formular perguntas: Digite sua pergunta na interface e clique no botão "Enviar Pergunta".
Obter respostas do LLM: O sistema utilizará o modelo LLM distilbert-base-uncased-distilled-squad para processar sua pergunta e gerar uma resposta com base nos arquivos de contexto carregados.
Visualizar respostas: A resposta do LLM será exibida na interface para sua análise.
Requisitos:
Python 3.6 ou superior
pip
Transformers
tkinter
Instalação:

Clone o repositório para o seu computador.
Instale as dependências usando o comando pip install -r requirements.txt.
Uso:

Execute o script llm_customer_support_gui.py.
Selecione uma pasta de arquivos de contexto usando o botão "Carregar Pasta".
Digite sua pergunta na caixa de texto e clique em "Enviar Pergunta".
A resposta do LLM será exibida na caixa de texto "Resposta".
Observações:

A precisão das respostas do LLM depende da qualidade e da relevância dos arquivos de contexto carregados.
Você pode ajustar o modelo LLM utilizado alterando a linha model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad") no script.
Este é um exemplo básico e pode ser adaptado para outras aplicações de suporte ao cliente com LLM.
Contribuições:

Sinta-se à vontade para contribuir com este projeto reportando bugs, sugerindo melhorias ou criando pull requests com suas próprias modificações.

Licença:

Este projeto está licenciado sob a licença MIT.
