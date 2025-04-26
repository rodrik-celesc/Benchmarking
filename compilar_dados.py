
import pandas as pd
import os
from glob import glob
from openpyxl import load_workbook

# Listar todos os arquivos Excel no diretório que iniciam com 'dados'
arquivos_excel = glob(os.path.join('**', 'dados*.xlsx'), recursive=True)

# Inicializar uma lista para armazenar os dataframes
dataframes = []

# Colunas em comum esperadas
colunas_comuns = ['Empresa', 'Conta', 'Código da Conta', 'Descrição da Conta']

arquivo = arquivos_excel[0]

# Carregar cada arquivo Excel e extrair as colunas necessárias
for arquivo in arquivos_excel:
    
    df = pd.read_excel(arquivo, engine='openpyxl')
    
    # Selecionar as colunas em comum e a última coluna numérica
    ultima_coluna = df.columns[-1]
    df = df[colunas_comuns + [ultima_coluna]]
    
    dataframes.append(df)

# Mesclar dataframes
merged_df = dataframes[0]
for df in dataframes[1:]:
    merged_df = pd.merge(merged_df, df, on=colunas_comuns, how='outer')

# Preencher valores NaN com 0
merged_df.fillna(0, inplace=True)

# Coluna ID 1
ID_1 = merged_df['Empresa'] + merged_df['Conta'] + merged_df['Código da Conta'] + merged_df['Descrição da Conta'].str.strip()

# Coluna ID 2
ID_2 = merged_df['Empresa'] + merged_df['Conta'] + merged_df['Descrição da Conta'].str.strip()

# Adicionar coluna ID no início do dataframe
merged_df.insert(0, 'ID 2', ID_2)
merged_df.insert(0, 'ID 1', ID_1)

# Salvar o dataframe mesclado em um novo arquivo Excel
output_file = 'CVM.xlsx'
merged_df.to_excel(output_file, sheet_name='dados', index=False)

# Configurar a coluna A como oculta e congelar a primeira linha
wb = load_workbook(output_file)
ws = wb['dados']

# Ocultar a coluna A
ws.column_dimensions['A'].hidden = True
ws.column_dimensions['B'].hidden = True

# Congelar a primeira linha
ws.freeze_panes = 'A2'

# Salvar as alterações no arquivo
wb.save(output_file)

# Fim do script
print("Arquivos compilados com sucesso")

