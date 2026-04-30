import streamlit as st
import pandas as pd
import os

# --------- File Paths (FIXED for Streamlit Cloud) ---------
folder_path = "data"
excel_file_path = "data/expense.csv"

# --------- Create Folder & File if Not Exists ---------
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(excel_file_path) or os.stat(excel_file_path).st_size == 0:
    expenses = pd.DataFrame(columns=["Date","Category","Description","Currency Type","Amount"])
    expenses.to_csv(excel_file_path, index=False)

# --------- UI Inputs ---------
st.title("💰 Expense Tracker")

date = st.date_input('Date 📅', key="da")

category = st.selectbox(
    "Category 📂",
    ("Housing","Utilities","Transportation","Food","Healthcare",
     "Insurance","Debt Payments","Entertainment","Personal Care",
     "Education","Savings","Taxes","Miscellaneous"),
    key="cat"
)

description = st.text_input('Description 🔍', key='desc')

currency_type = st.selectbox("Currency 💲 / 💶", ("Dollars","Euros"))

amount = st.number_input('Amount 💵', key='am', min_value=0, step=1, max_value=20000)

# --------- Functions ---------
def clear():
    st.session_state.am = 0
    st.session_state.desc = ""

def insert(date, category, description, currency_type, amount):
    dataframe = pd.read_csv(excel_file_path)
    length = len(dataframe)

    if description.strip() != "" and amount > 0:
        dataframe.loc[length] = [date, category, description, currency_type, amount]
        dataframe.to_csv(excel_file_path, index=False)
        st.success("Expense added successfully!")
        st.balloons()
    else:
        st.error("Please provide a description and a valid amount greater than zero.")

# --------- Buttons Layout ---------
col1, col2 = st.columns([0.3, 0.7])

with col1:
    add = st.button("Add Expense 💸")

with col2:
    clear_button = st.button("Clear ✂️", on_click=clear)

# --------- Action ---------
if add:
    insert(date, category, description, currency_type, amount)

# --------- Show Data ---------
st.subheader("📊 Expense Records")

try:
    df = pd.read_csv(excel_file_path)
    st.dataframe(df)
except:
    st.info("No data available yet.")


