import pandas as pd

# Caminho do arquivo
file_path = r"/planilha/consumo_aparelhos.xlsx"

# Leia o arquivo Excel
df = pd.read_excel(file_path)

# Exibe as primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df.head())

# Soma dos valores de uma coluna específica
total_custo = df['Custo Mensal (R$)'].sum()
print(f"\nCusto Mensal Total: R$ {total_custo:.2f}")

# Iterar sobre as linhas para acessar cada dado
print("\nIteração sobre cada linha:")
for index, row in df.iterrows():
    print(f"Linha {index}: {row.to_dict()}")
    
# Acessar uma célula específica
linha = 0  # Índice da linha
coluna = 'Custo Mensal (R$)'  # Nome da coluna
valor_celula = df.at[linha, coluna]
print(f"\nValor na linha {linha} e coluna '{coluna}': R$ {valor_celula}")

# Obter uma coluna inteira
coluna_custo = df['Custo Mensal (R$)']
print("\nValores da coluna 'Custo Mensal (R$)':")
print(coluna_custo)

# Obter valores únicos de uma coluna
valores_unicos = df['Custo Mensal (R$)'].unique()
print("\nValores únicos na coluna 'Custo Mensal (R$)':")
print(valores_unicos)

# Filtrar linhas com base em uma condição
condicao = df['Custo Mensal (R$)'] > 100
filtrado = df[condicao]
print("\nLinhas com custo mensal maior que R$ 100:")
print(filtrado)