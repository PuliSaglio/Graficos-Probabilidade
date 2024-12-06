import pandas as pd
import matplotlib.pyplot as plt

academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

print(academic_performance_df['Física'].isnull().sum())

# Verificar estatísticas da coluna
print(academic_performance_df['Física'].describe())

plt.hist(academic_performance_df['Física'], bins=10, edgecolor='black', color='skyblue')
plt.title('Histograma das Notas de Física')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


