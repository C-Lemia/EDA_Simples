import pandas as pd
import numpy as np


# Novos dados fictícios
novos_dados = {
    'Nome': ['Daniel', 'Victoria', 'Samuel', 'Sophia', 'Leon', 'Isabella', 'Henry', 'Olivia', 'David', 'Emma',
             'Liam', 'Mia', 'Lucas', 'Charlotte', 'Ethan', 'Amelia', 'Noah', 'Ava', 'Benjamin', 'Harper'],
    'Idade': [33, 27, 42, 29, 31, 20, 48, 19, 34, 21, 40, 25, 45, 30, 28, 22, 36, 33, 43, 24],
    'Sexo': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino',
             'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino'],
    'Classe': np.random.randint(1, 4, size=20),  # Gera classes entre 1 e 3
    'Sobrevivente': np.random.randint(0, 2, size=20)  # Gera 0 (não sobreviveu) ou 1 (sobreviveu)
}

# Criar DataFrame com os novos dados e concatenar com o original
df_total = pd.DataFrame(novos_dados)

df_total['Classe'] = df_total['Classe'].replace({1: 'A', 2: 'B', 3: 'C'})

# Exibir o novo DataFrame
print(df_total.head(10))  # Mostrar as 10 primeiras linhas para visualização
