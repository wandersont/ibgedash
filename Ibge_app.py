import streamlit as st
import pandas as pd
import importlib
import ibge_utilities
importlib.reload(ibge_utilities)

st.write('# Dashboard prototype - Brazilian economic data (IBGE)')
st.write('This is a single demo for brazilian economic data extracted from IBGE.')
st.write('Further data optmizations need to be implemented.')
