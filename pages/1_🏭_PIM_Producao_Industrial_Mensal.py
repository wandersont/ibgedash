import streamlit as st
import pandas as pd
import ibge_utilities
import importlib
importlib.reload(ibge_utilities)

st.set_page_config(
    page_title='PIM - Produção Industrial Mensal',
    page_icon='🏭'
)

@st.cache_data
def draw_main_chart():
    dados = ibge_utilities.get_pim()['1 Indústria geral']
    st.title('PIM Índice Geral (2022=100)')
    st.line_chart(data=dados, y='V')

draw_main_chart()