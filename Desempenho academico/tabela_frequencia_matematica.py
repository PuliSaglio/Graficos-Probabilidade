import pandas as pd

# Ler os dados
academic_performance_df = pd.read_csv('Graficos/Academic_Performance.csv')

# Verificar valores ausentes
academic_performance_df['Matemática'].fillna(0, inplace=True)

# Garantir valores no intervalo [0, 10]
academic_performance_df = academic_performance_df[
    (academic_performance_df['Matemática'] >= 0) & (academic_performance_df['Matemática'] <= 10)
]

# Criar intervalos
intervalos = [0, 2, 4, 6, 8, 10.1]  # Adicionar 10.1 para incluir o limite superior
academic_performance_df['Intervalo_Matemática'] = pd.cut(
    academic_performance_df['Matemática'], bins=intervalos, right=False
)

# Calcular frequências
frequencia_intervalos = academic_performance_df['Intervalo_Matemática'].value_counts().sort_index()

# Criar tabela de frequência
tabela_frequencia = pd.DataFrame({
    'Frequência Absoluta': frequencia_intervalos,
    'Frequência Relativa': frequencia_intervalos / len(academic_performance_df),
    'Frequência Percentual (%)': (frequencia_intervalos / len(academic_performance_df)) * 100
})

# Verificar soma das frequências
print(f"A soma da frequência absoluta é: {tabela_frequencia['Frequência Absoluta'].sum()}")
print(f"A soma da frequência percentual é: {tabela_frequencia['Frequência Percentual (%)'].sum():.2f}%")

# Exibir tabela
print(tabela_frequencia)
