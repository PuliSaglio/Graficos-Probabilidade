import pandas as pd
import matplotlib.pyplot as plt

academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

media_biologia_por_turno = academic_performance_df.groupby('Turno')['Biologia'].mean().reset_index()

print(media_biologia_por_turno)

# Gráfico de barras
plt.bar(media_biologia_por_turno['Turno'], media_biologia_por_turno['Biologia'], color='skyblue', edgecolor='black')
plt.title('Média das Notas de Biologia por Turno')
plt.xlabel('Turno')
plt.ylabel('Média das Notas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
