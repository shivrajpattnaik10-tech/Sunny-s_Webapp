import streamlit as st
import pandas as pd
import time,os

folder_path="/workspaces/codespaces-blank/data"
excel_file_path ="/workspaces/codespaces-blank/data/expense.csv"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(excel_file_path) or os.stat(excel_file_path).st_size == 0:
    expenses = pd.DataFrame(columns=["Date","Category","Description","Currency Type","Amount"])
    expenses.to_csv(excel_file_path,index=False)

date = st.date_input('Date :date:',key="da")

category = st.selectbox("Category :card_index_dividers:",("Housing","Utilities","Transportation","Food","Healthcare","Insurance","Debt Payments","Entertainment","Personal Care","Education","Savings","Taxes","Miscellaneous"),key="cat")

description=st.text_input('Description :flashlight:',key='desc')

currency_type = st.selectbox("Currency type :heavy_dollar_sign: /  :euro:",("Dollars","Euros"))

amount=st.number_input('Amount :money_mouth_face:',key='am',min_value=0,step=1,max_value=20000)

def clear():
    st.session_state.am=0
    st.session_state.desc=""

def insert(date,category,description,currency_type,amount):
    dataframe=pd.read_csv(excel_file_path)
    length=len(dataframe)
    if description!="" and amount>0:
        dataframe.loc[length]=[date,category,description,currency_type,amount]
        dataframe.to_csv(excel_file_path,index=False)
        st.balloons()
    else:
        st.error("Please provide a description and a valid amount value greater than zero.")

col1,col2 = st.columns([0.24,0.9])

with col1:
    add = st.button("Add Expense :money_with_wings:")
with col2:
    clear_button = st.button("Clear :scissors:",on_click=clear)

if add:
    insert(date,category,description,currency_type,amount)