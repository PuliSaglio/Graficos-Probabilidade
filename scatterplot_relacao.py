import pandas as pd
import matplotlib.pyplot as plt

service_satisfaction_df = pd.read_csv('Graficos/Service_Satisfaction.csv')

# Calcular a média das avaliações
service_satisfaction_df['Média_Avaliações'] = service_satisfaction_df[['Atendimento', 'Infraestrutura', 'Eficiência']].mean(axis=1)

# Criar o scatterplot
plt.scatter(service_satisfaction_df['Renda (R$)'], service_satisfaction_df['Média_Avaliações'], alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Relação entre Renda e Média das Avaliações')
plt.xlabel('Renda')
plt.ylabel('Média das Avaliações')
plt.grid(alpha=0.3)
plt.show()

