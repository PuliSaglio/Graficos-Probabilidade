import pandas as pd
from scipy import stats

academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

media = academic_performance_df['Matemática'].mean()
print(f"Média: {media}")

mediana = academic_performance_df['Matemática'].median()
print(f"Mediana: {mediana}")

moda = stats.mode(academic_performance_df['Matemática'], keepdims=True).mode[0]
print(f"Moda: {moda}")

desvio_padrao = academic_performance_df['Matemática'].std()
print(f"Desvio Padrão: {desvio_padrao}")

amplitude = academic_performance_df['Matemática'].max() - academic_performance_df['Matemática'].min()
print(f"Amplitude: {amplitude}")