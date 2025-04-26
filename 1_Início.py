
# MÓDULOS
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title='Benchmarking Celesc',
    page_icon=':zap:',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://www.celesc.com.br/',
        'Report a bug': 'https://www.celesc.com.br/',
        'About': 'Departamento de Controle de Resultados e Planejamento Financeiro (DPCL)'
    }
)

# LOGO
logo = Image.open('./imagens/logo_1.png')
st.sidebar.image(logo, width=200)

# TÍTULO BARRA LATERAL
st.title('Benchmarking Celesc')

# IMPORTAR DADOS
@st.cache_data
def dados():
    
    # Importar
    df =  pd.read_excel(
        io='./base_de_dados.xlsx',
        sheet_name='dados',
        engine='openpyxl'
    )
    
    # Selecionar colunas numéricas não nulas
    colunas_numericas = df.select_dtypes(include=['int64']).columns.tolist()
    
    # Excluir linhas onde todas as colunas numéricas são zero
    df = df[df[colunas_numericas].ne(0).any(axis=1)]
    
    # Colunas principais
    colunas_principais = df.columns[:4].tolist()
    
    # Selecionar colunas
    colunas_selecionadas = colunas_principais + colunas_numericas
    
    # Filtro
    df = df[colunas_selecionadas]
    
    # Transformar colunas numéricas em uma única coluna chamada Ano
    df = df.melt(
        id_vars=colunas_principais, 
        value_vars=colunas_numericas, 
        var_name='Ano', 
        value_name='Valor'
    )
    
    # Converter a coluna 'Ano' para o tipo string
    df['Ano'] = df['Ano'].astype(str)
    
    return df

# GRAVAR DADOS NA SESSÃO
dados = dados()
st.session_state['dados'] = dados

dados
