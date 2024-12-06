import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ler os dados
satisfaction_df = pd.read_csv('Graficos/Service_Satisfaction.csv')

# Calcular as medidas de dispersão
media_renda = satisfaction_df['Renda (R$)'].mean()
mediana_renda = satisfaction_df['Renda (R$)'].median()
desvio_padrao_renda = satisfaction_df['Renda (R$)'].std()
amplitude_renda = satisfaction_df['Renda (R$)'].max() - satisfaction_df['Renda (R$)'].min()

print(f"Média: {media_renda}")
print(f"Mediana: {mediana_renda}")
print(f"Desvio Padrão: {desvio_padrao_renda}")
print(f"Amplitude: {amplitude_renda}")

# Calcular Q1, Q3 e IQR
q1 = satisfaction_df['Renda (R$)'].quantile(0.25)
q3 = satisfaction_df['Renda (R$)'].quantile(0.75)
iqr = q3 - q1

# Limites para outliers
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Identificar outliers
outliers = satisfaction_df[(satisfaction_df['Renda (R$)'] < limite_inferior) | (satisfaction_df['Renda (R$)'] > limite_superior)]
print(f"\nOutliers detectados:\n{outliers}")

# Visualizar com Boxplot
plt.boxplot(satisfaction_df['Renda (R$)'], vert=False, patch_artist=True)
plt.title('Boxplot da Renda')
plt.xlabel('Renda')
plt.show()
