
import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def main():
    df_raw = load_data()

    st.dataframe(df_raw)

def create_dataframe_section(df):

if __name__ == '__main__':
    main()


# Função que irá criar 
def create_sorted_companies_tuple(dataframe):
    companies = dataframe['company_name'].to_list()
    
    companies_aux = [ company.split(' ') for company in companies ]
    
    companies_aux.sort(key=len, reverse=True)
    
    sorted_companies = [ ' '.join(company) for company in companies_aux ]
    
    return tuple(sorted_companies)