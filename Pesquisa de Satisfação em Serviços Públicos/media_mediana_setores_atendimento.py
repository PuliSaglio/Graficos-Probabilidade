import pandas as pd

# Ler os dados
academic_performance_df = pd.read_csv('Graficos/Service_Satisfaction.csv')


# Calcular as métricas
estatisticas = academic_performance_df['Eficiência'].agg(['mean', 'median' ,'std'])

# Adicionar coeficiente de variação
estatisticas.loc['Coeficiente_Variacao'] = estatisticas.loc['std'] / estatisticas.loc['mean']

# Resultados
print(estatisticas)
