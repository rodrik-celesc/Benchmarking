
# MÓDULOS
import streamlit as st
import pandas as pd
import time
from streamlit_option_menu import option_menu

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


# BARRA LATERAL
# with st.sidebar:
select = option_menu(
    menu_title='Estrutura de Capital',
    options=[
        'Divida Total Liquida', 
        'Divida Total Bruta'
        ],
    icons=[
        'house', 
        'bar-chart'
        ],
    default_index=0,
    orientation='horizontal',
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