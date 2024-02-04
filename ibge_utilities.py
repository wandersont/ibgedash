import pandas as pd
import requests
from datetime import datetime

def get_pim():
    pim_df = pd.DataFrame(requests.get('https://apisidra.ibge.gov.br/values/t/8888/P/all/V/12606/C544/all/N1/1').json())
    pim_df = pim_df[1:]
    pim_df['mes_ref'] = pim_df['D1C'].apply(lambda x: datetime(int(x[:4]), int(x[4:]), 1))
    categorias = pim_df['D3N'].unique()
    cat_data = {}
    for cat in categorias:
        pre_data = pim_df[pim_df['D3N']==cat][['V', 'mes_ref']].set_index('mes_ref')
        pre_data['V'] = pre_data['V'].apply(lambda x: float(x) if x!='-' else None)
        cat_data[cat] = pre_data
    return cat_data

def get_pmc():
    pmc_df = pd.DataFrame(requests.get('https://apisidra.ibge.gov.br/values/t/8880/P/all/V/7169/C11046/56734/N1/1').json())
    pmc_df = pmc_df[1:]
    pmc_df['mes_ref'] = pmc_df['D1C'].apply(lambda x: datetime(int(x[:4]), int(x[4:]), 1))
    pmc_df = pmc_df[['mes_ref', 'V']]
    pmc_df = pmc_df.set_index('mes_ref')
    pmc_df['V'] = pmc_df['V'].apply(lambda x: float(x) if x!='-' else None)
    return pmc_df