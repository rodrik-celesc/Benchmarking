
import os
import pdfplumber
import pandas as pd

# Lista para armazenar todos os dados
dados_cvm = []

# Iterar sobre os arquivos na pasta
for arquivo in os.listdir():
    
    if arquivo.endswith('.pdf'):
        
        # Abrir e extrair texto do PDF
        with pdfplumber.open(arquivo) as pdf:
            
            # Iniciar variável conta
            conta = None
            
            for pagina in pdf.pages:
                
                texto = pagina.extract_text()
                linhas = texto.split('\n')

                # Identificar a aba conta com base no texto
                if 'DFs Individuais / Balanço Patrimonial Ativo' in texto:
                    conta = 'Ativo'
                elif 'DFs Individuais / Balanço Patrimonial Passivo' in texto:
                    conta = 'Passivo'
                elif 'DFs Individuais / Demonstração do Resultado' in texto:
                    conta = 'Resultado'
                else:
                    conta = None

                # Processar os dados apenas se estiver em uma aba válida
                if conta:
                    for i, linha in enumerate(linhas):
                        
                        # Extrair o ano e o nome da empresa
                        titulo = linhas[0]
                        
                        # Extrair o ano
                        ano_atual = int(titulo.split(' - ')[2].split('/')[2])
                        ano_anterior = ano_atual - 1
                        
                        # Extrair o nome da empresa
                        empresa = titulo.split(' - ')[3].split('Versão')[0]  
                
                        # Tabela com 3 anos
                        if 'Código da Descrição da Conta Último Exercício Penúltimo Exercício Antepenúltimo Exercício' in linha:
                            
                            
                            # Processar as linhas
                            for dados in linhas[i + 1:]:
                                colunas = dados.split()
                                
                                if len(colunas) >= 5:
                                
                                    # Colunas numéricas 
                                    exercicio_atual = colunas[-3].replace('.', '').replace(',', '.')
                                    exercicio_anterior = colunas[-2].replace('.', '').replace(',', '.')

                                    # Adicionar espaços na descrição
                                    codigo = colunas[0]
                                    descricao = ' '.join(colunas[1:-3])
                                    nivel_indentacao = codigo.count('.')
                                    descricao = ('    ' * nivel_indentacao) + descricao

                                    linha_dados = {
                                        'Empresa': empresa,
                                        'Conta': conta,
                                        'Código da Conta': codigo,
                                        'Descrição da Conta': descricao,
                                        str(ano_anterior): float(exercicio_anterior) if exercicio_anterior.replace('-', '').isdigit() else None,
                                        str(ano_atual): float(exercicio_atual) if exercicio_atual.replace('-', '').isdigit() else None
                                    }
                                    
                                    dados_cvm.append(linha_dados)
                                
                                else:
                                    continue
                        
                        # Tabela com 2 anos
                        elif 'Código da Descrição da Conta Último Exercício Penúltimo Exercício' in linha:
                            
                            # Processar as linhas
                            for dados in linhas[i + 1:]:
                                colunas = dados.split()
                                
                                if len(colunas) >= 4:
                                
                                    # Colunas numéricas 
                                    exercicio_atual = colunas[-2].replace('.', '').replace(',', '.')
                                    exercicio_anterior = colunas[-1].replace('.', '').replace(',', '.')

                                    # Adicionar espaços na descrição
                                    codigo = colunas[0]
                                    descricao = ' '.join(colunas[1:-2])
                                    nivel_indentacao = codigo.count('.')
                                    descricao = ('    ' * nivel_indentacao) + descricao

                                    linha_dados = {
                                        'Empresa': empresa,
                                        'Conta': conta,
                                        'Código da Conta': codigo,
                                        'Descrição da Conta': descricao,
                                        str(ano_anterior): float(exercicio_anterior) if exercicio_anterior.replace('-', '').isdigit() else None,
                                        str(ano_atual): float(exercicio_atual) if exercicio_atual.replace('-', '').isdigit() else None
                                    }
                                    
                                    dados_cvm.append(linha_dados)
                                
                                else:
                                    continue
                            
                                    

# Criar um DataFrame com todos os dados
df_geral = pd.DataFrame(dados_cvm)

# Filtro para eliminar linhas desnecessárias do Resultado
df_geral = df_geral[~((df_geral['Conta'] == 'Resultado') & (df_geral['Código da Conta'] > '3.11'))]

# Filtro para eliminar linhas com código "Conta"
df_geral = df_geral[(df_geral['Código da Conta'] != 'Conta') & (df_geral['Código da Conta'] != 'PÁGINA:')]

# Nome arquivo
nome_arquivo = 'dados ' + str(ano_atual) + '.xlsx'

# Salvar os dados em Excel
df_geral.to_excel(nome_arquivo, sheet_name='dados', index=False)

print('Processamento Concluído!!!')

