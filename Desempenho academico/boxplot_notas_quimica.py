import pandas as pd
import matplotlib.pyplot as plt

academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')


# Verificar dados ausentes ou fora do intervalo
print(academic_performance_df['Química'].isnull().sum())
print(academic_performance_df['Química'].describe())

plt.boxplot(academic_performance_df['Química'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Boxplot das Notas de Química')
plt.xlabel('Notas')
plt.show()

