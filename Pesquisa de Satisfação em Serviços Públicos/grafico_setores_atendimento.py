import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Graficos/Service_Satisfaction.csv')

avaliacoes_altas = df[df['Atendimento'] >= 4]

# Calcular o total de avaliações e a quantidade de altas
total_avaliacoes = len(df)
quantidade_altas = len(avaliacoes_altas)

# Calcular a porcentagem
percentual_altas = (quantidade_altas / total_avaliacoes) * 100
percentual_baixas = 100 - percentual_altas

# Dados para o gráfico
labels = ['Avaliações 4 ou 5', 'Outras Avaliações']
sizes = [percentual_altas, percentual_baixas]
colors = ['skyblue', 'lightgray']
explode = (0.1, 0)  # Destaque para o primeiro segmento

# Criar o gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='black'))

# Título
plt.title('Porcentagem de Avaliações Altas em Atendimento')
plt.show()