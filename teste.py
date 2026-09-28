
# %%
import pandas as pd
df = pd.read_excel('Campeoes.xlsx')
df

# %%
features = ['Dano','Tipo',	'Range',	'Sexo',	'Mana'	]
target = 'Nome'
x = df[features]
y = df[target]
x = x.replace({'Ap':1,
              'Ad':2,
              'Mago':1,
              'Assasino':2,
              'Lutador':3,
              'Atirador':4,
              'Masculino':1,
              'Feminino':2,
              'Sim':1,
              'Não':2,
              'Curto':1,
              'Longo':2
              })

# %%
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(x,y)

# %%
# ==========================================
# 4. INTERAÇÃO COM O USUÁRIO PELO CONSOLE
# ==========================================
print("--- Descubra o Campeão ---")
print("Responda às perguntas abaixo (Exatamente como nas opções):")

# Coletando e convertendo a variável 'Dano'
resp_dano = input("Qual o tipo de dano (Ap / Ad)? ").strip().capitalize()
dano_num = 1 if resp_dano == 'Ap' else 2

# Coletando e convertendo a variável 'Tipo'
resp_tipo = input("Qual a classe (Mago / Assasino / Lutador / Atirador)? ").strip().capitalize()
mapa_tipo = {'Mago': 1, 'Assasino': 2, 'Lutador': 3, 'Atirador': 4}
tipo_num = mapa_tipo.get(resp_tipo, 1) # Padrão para Mago caso o usuário digite errado

# Coletando e convertendo a variável 'Range'
resp_range = input("Qual o alcance (Curto / Longo)? ").strip().capitalize()
range_num = 1 if resp_range == 'Curto' else 2

# Coletando e convertendo a variável 'Sexo'
resp_sexo = input("Qual o gênero (Masculino / Feminino)? ").strip().capitalize()
sexo_num = 1 if resp_sexo == 'Masculino' else 2

# Coletando e convertendo a variável 'Mana'
resp_mana = input("O personagem usa mana (Sim / Não)? ").strip().capitalize()
mana_num = 1 if resp_mana == 'Sim' else 2

# 5. Fazer a previsão com os dados inseridos
caracteristicas_usuario = [[dano_num, tipo_num, range_num, sexo_num, mana_num]]
previsao = model.predict(caracteristicas_usuario)

print("\n==============================")
print(f"O modelo previu o campeão: {previsao[0]}")
print("==============================")
