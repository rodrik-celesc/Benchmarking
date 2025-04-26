


def estrutura_capital_1():
    
    ''' Dívida Bruta / Ativo Total '''
    
    import streamlit as st
    import altair as alt
    
    # Importar dados
    dados = st.session_state['dados']
    
    # Cálculo do indicador
    divida_bruta = dados[dados['Descrição da Conta'] == 'Empréstimos e Financiamentos'].groupby(['Empresa', 'Ano'])['Valor'].sum()
    ativo_total = dados[dados['Descrição da Conta'] == 'Ativo Total'].groupby(['Empresa', 'Ano'])['Valor'].sum()
    indicador = divida_bruta / ativo_total * 100

    # Renomear o índice
    indicador = indicador.reset_index()

    # Excluir empresas com valores nulos no indicador
    indicador = indicador.dropna(subset=['Valor'])
    
    # Gráfico
    grafico = alt.Chart(indicador).mark_line().encode(
    x=alt.Y('Ano', title=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Valor', title=None),
    color=alt.Color('Empresa', legend=alt.Legend(orient='bottom')),
    tooltip=['Ano', 'Empresa', 'Valor']
    ).properties(
        width=700,
        height=400,
        title='Dívida Bruta / Ativo Total'
    ).interactive()

    return st.altair_chart(grafico, use_container_width=True)





