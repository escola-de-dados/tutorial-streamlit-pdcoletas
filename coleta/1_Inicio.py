import streamlit as st
import pandas as pd
import webbrowser as wb

#Configura detalhes da página
st.set_page_config(
    page_title="Início",
    page_icon="♻️",
)

DATA_URL = ('https://raw.githubusercontent.com/anicelysantos/codabr23-streamlit/main/pontos-coleta-recife.csv')

dados = pd.read_csv(DATA_URL)

#constroi um "cache" dos dados
st.session_state["dados"] = dados

st.title('Pontos de coleta em Recife')

st.markdown(''' ### O Lixo é responsabilidade de todos''')
st.markdown('''Você já parou para pensar o que acontece com o lixo que sai da sua casa? E que o futuro desse material 
            depende muito da sua atitude? Quando o cidadão encaminha o lixo para a reciclagem, além de evitar mais acúmulo 
            de material nos aterros, garante que menos recursos naturais sejam extraídos para a fabricação de outros produtos e 
            contribui para a geração de emprego e renda de muitos trabalhadores¹.''') 
            
st.markdown('O gráfico abaixo mostra a quantidade de pontos de coleta por região.')

#Sumariza as regiões
qt_regiao = dados['regiao'].value_counts()

#Mostra a sumarização em um gráfico
st.bar_chart(qt_regiao, color='#006400')

#Constrói um mapa com os dados
st.map(dados)

col1,col2 = st.columns(2)
btn1 = col1.button('Dados da prefeitura do Recife', use_container_width=True)
if btn1:
    wb.open_new_tab("http://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos")
btn2 = col2.button('Dados limpos', use_container_width=True)
if btn2:
    wb.open_new_tab("https://github.com/anicelysantos/codabr23-streamlit/blob/main/pontos-coleta-recife.csv")
