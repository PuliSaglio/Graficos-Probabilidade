import pandas as pd

# Ler os dados
academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

# Selecionar as colunas de notas
disciplinas = ['Matemática', 'Física', 'Química', 'Biologia']

# Calcular as métricas
estatisticas = academic_performance_df[disciplinas].agg(['mean','std'])

# Adicionar coeficiente de variação
estatisticas.loc['Coeficiente_Variacao'] = estatisticas.loc['std'] / estatisticas.loc['mean']

# Identificar disciplinas com maior dispersão
maior_dispersao_dp = estatisticas.loc['std'].idxmax()
maior_dispersao_cv = estatisticas.loc['Coeficiente_Variacao'].idxmax()

# Resultados
print(estatisticas)
print("\n")
print(f"A disciplina com maior dispersão (Desvio Padrão) é: {maior_dispersao_dp}")
print(f"A disciplina com maior dispersão relativa (Coeficiente de Variação) é: {maior_dispersao_cv}")
