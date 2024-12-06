import pandas as pd
from scipy.stats import skew

# Ler os dados
academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

# Selecionar as colunas de notas
disciplinas = ['Matemática', 'Física', 'Química', 'Biologia']

# Calcular a assimetria
assimetria = academic_performance_df[disciplinas].apply(skew)

# Identificar disciplinas com assimetria significativa
disciplinas_assimetricas = assimetria[assimetria.abs() > 0.5]

# Exibir os resultados
print("Assimetria das disciplinas:")
print(assimetria)

print("\nDisciplinas com assimetria significativa:")
print(disciplinas_assimetricas)
