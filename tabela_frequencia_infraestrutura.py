import pandas as pd

df = pd.read_csv('Graficos/Service_Satisfaction.csv')

frequencia = df['Infraestrutura'].value_counts().sort_index()

tabela_frequencia = pd.DataFrame({
    'Frequência Absoluta': frequencia,
    'Frequência Relativa': frequencia/ len(df),
    'Frequência Percentual (%)': frequencia/len(df) *100
})

print(f"A soma da frequência absoluta é: {tabela_frequencia['Frequência Absoluta'].sum()}")
print(f"A soma da frequência percentual é: {tabela_frequencia['Frequência Percentual (%)'].sum():.2f}%")

print(tabela_frequencia)