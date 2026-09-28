🎮 Adivinhador de Campeões (Machine Learning) 🤖⚔️

Bem-vindo ao Adivinhador de Campeões! Este projeto é uma aplicação de linha de comando (CLI) baseada em Python que funciona como um "Akinator" para personagens. Utilizando Machine Learning (Árvore de Decisão), o programa faz perguntas sobre as características de um campeão e adivinha qual personagem você tem em mente!

✨ Funcionalidades

Interatividade no Terminal: O usuário responde a perguntas simples diretamente pelo console.

Machine Learning na Prática: Utiliza o algoritmo DecisionTreeClassifier da biblioteca Scikit-Learn para classificar e prever o campeão.

Tratamento de Dados: Conversão de variáveis categóricas (texto) para dados numéricos compreensíveis pelo modelo.

🛠️ Tecnologias Utilizadas

Python - Linguagem principal.

Pandas - Para leitura e manipulação da base de dados (.xlsx).

Scikit-Learn - Para a criação e treinamento do modelo de Inteligência Artificial.

⚙️ Como o Código Funciona (Processo)

O script foi desenvolvido seguindo o pipeline clássico de um projeto de Machine Learning:

Coleta de Dados:
O Pandas lê o arquivo Excel (dados/Campeoes.xlsx) contendo as características de vários campeões.

Separação de Variáveis (Features e Target):

Features (X): Dano, Tipo, Range, Sexo, Mana. Estas são as "pistas" que o modelo usará para aprender.

Target (Y): Nome. É a resposta final que queremos prever.

Pré-processamento de Dados:
Como algoritmos de Machine Learning lidam melhor com números, transformamos as categorias de texto em valores numéricos utilizando a função .replace(). Por exemplo: 'Ap' vira 1, 'Ad' vira 2.

Treinamento do Modelo:
Instanciamos o DecisionTreeClassifier (Árvore de Decisão) e usamos o método .fit(x, y) para ensinar o modelo a relacionar as características (features) ao nome do campeão (target).

Interação e Previsão:

O sistema coleta as respostas do usuário via input().

Limpa e padroniza as respostas (usando .strip().capitalize()).

Converte as respostas de volta para a linguagem numérica do modelo.

Executa a previsão final .predict() e exibe o resultado no console!

🚀 Como Executar o Projeto

Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Você também precisará instalar as bibliotecas dependentes.

# Clone este repositório
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

# Entre na pasta do projeto
cd NOME_DO_REPOSITORIO

# Instale as dependências necessárias
pip install pandas scikit-learn openpyxl


Estrutura de Arquivos

Certifique-se de que a sua estrutura de pastas está assim antes de rodar o código:

📦 seu-repositorio
 ┣ 📂 dados
 ┃ ┗ 📜 Campeoes.xlsx      <-- Sua base de dados
 ┣ 📜 main.py              <-- Script principal
 ┗ 📜 README.md


Rodando o programa

Basta executar o script Python no seu terminal:

python main.py


Responda às perguntas e veja a mágica acontecer! ✨

🤝 Contribuições

Sinta-se à vontade para fazer um Fork deste projeto e enviar Pull Requests com melhorias, como adicionar novos campeões à base de dados ou implementar uma interface gráfica (GUI).

Feito com 💻 e ☕!
