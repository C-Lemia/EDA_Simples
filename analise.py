import seaborn as sns
import matplotlib.pyplot as plt
import dados  # Importa o script dados.py

# Acessa df_total diretamente
df_total = dados.df_total

# Verificar se há dados faltantes
dados_faltantes = df_total.isnull().sum()

# Resumo estatístico dos dados
resumo_estatistico = df_total.describe()

# Distribuição de sobrevivência por classe
plt.figure(figsize=(8, 6))
sns.countplot(data=df_total, x='Classe', hue='Sobrevivente')
plt.title('Distribuição de Sobreviventes por Classe')
plt.xlabel('Classe')
plt.ylabel('Número de Passageiros')
plt.legend(title='Sobrevivente', loc='upper right')
plt.show()

# Visualizar correlação entre idade e sobrevivência
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_total, x='Sobrevivente', y='Idade')
plt.title('Distribuição de Idade entre Sobreviventes e Não Sobreviventes')
plt.xlabel('Sobrevivente')
plt.ylabel('Idade')
plt.show()

# Verificar a correlação entre as variáveis numéricas
correlacao = df_total.corr()
print(correlacao)
