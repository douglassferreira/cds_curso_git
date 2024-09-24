
import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def main():
    df_raw = load_data()

    create_dataframe_section(df)

    create_answers_section(df)

    return None



if __name__ == '__main__':
    main()

def create_answers_section(df): 
    st.title("Main Questions Answers")
    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")
    st.subheader("How many bikes are being sold are bikes from a unique owner?")
    st.subheader("Are high kilometer bikes more expensive than bikes with lower kilometer?")
    return None

# Função que irá criar 
def create_sorted_companies_tuple(dataframe):
    companies = dataframe['company_name'].to_list()
    
    companies_aux = [ company.split(' ') for company in companies ]
    
    companies_aux.sort(key=len, reverse=True)
    
    sorted_companies = [ ' '.join(company) for company in companies_aux ]
    
    return tuple(sorted_companies)
