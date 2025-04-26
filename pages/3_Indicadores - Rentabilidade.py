
# MÓDULOS
import streamlit as st
from streamlit_option_menu import option_menu
import indicadores as ind

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title='Benchmarking Celesc',
    page_icon=':bar_chart:',
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://www.celesc.com.br/',
        'Report a bug': 'https://www.celesc.com.br/',
        'About': 'Departamento de Controle de Resultados e Planejamento Financeiro (DPCL)'
    }
)

# --------------------------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------------------------
with st.sidebar:
    selecao = option_menu(
        menu_title=None,
        options=[
            'Dívida Bruta / Ativo Total', 
            'Dívida Bruta / Patr. Líq.',
            'Dívida Líquida / Patr. Líq.',
            'Dívida CP / Dívida Total'
            ],
        icons=[
            'bar-chart', 
            'bar-chart',
            'bar-chart',
            'bar-chart'
            ],
        default_index=0,
        orientation='vertical',
        styles={
            'container': {
                'padding': '5!important', 
                'background-color': '#f0f2f6'
                },
            'icon': {
                'color': '#1f77b4', 
                'font-size': '14px'
                },
            'nav-link': {
                'font-size': '12px', 
                'text-align': 'left', 
                'margin': '2px', 
                '--hover-color': '#e8f4fd'
                },
            'nav-link-selected': {
                'background-color': '#1f77b4', 
                'color': 'white'
                },
        }
    )