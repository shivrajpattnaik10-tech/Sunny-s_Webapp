import streamlit as st
import pandas as pd
import os

# --------- Correct File Path ---------
folder_path = "data"
excel_file_path = "data/expense.csv"

# --------- Ensure file exists ---------
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(excel_file_path):
    df = pd.DataFrame(columns=["Date","Category","Description","Currency Type","Amount"])
    df.to_csv(excel_file_path, index=False)

def execution():
    try:
        dataframe = pd.read_csv(excel_file_path)
    except Exception as e:
        st.error("Error reading file")
        return

    # --------- Handle empty file ---------
    if dataframe.empty:
        st.warning("No expenses added yet.")
        return

    # --------- Convert Date safely ---------
    dataframe["Date"] = pd.to_datetime(dataframe["Date"], errors='coerce')
    dataframe = dataframe.dropna(subset=["Date"])

    if dataframe.empty:
        st.error("No valid data found in CSV")
        return

    # --------- Total ---------
    total = dataframe["Amount"].sum()
    st.subheader(f"Gold coins: {int(total)//200} 🪙")

    # --------- Filters ---------
    date_from = st.date_input("From Date 📅", dataframe["Date"].min())
    date_to = st.date_input("To Date 📅", dataframe["Date"].max())

    amount_min = st.slider("Minimum value", 0, 20000, 0, 10)
    amount_max = st.slider("Maximum value", 0, 20000, 20000, 10)

    category = st.multiselect(
        "Categories 🗂️",
        ["Housing","Utilities","Transportation","Food","Healthcare","Insurance",
         "Debt Payments","Entertainment","Personal Care","Education",
         "Savings","Taxes","Miscellaneous"]
    )

    # --------- Apply filters ---------
    filtered_df = dataframe[
        (dataframe["Date"] >= pd.to_datetime(date_from)) &
        (dataframe["Date"] <= pd.to_datetime(date_to)) &
        (dataframe["Amount"] >= amount_min) &
        (dataframe["Amount"] <= amount_max)
    ]

    if category:
        filtered_df = filtered_df[filtered_df["Category"].isin(category)]

    # --------- Display ---------
    st.dataframe(filtered_df)

    # --------- Chart ---------
    if not filtered_df.empty:
        chart_data = filtered_df.groupby("Category")["Amount"].sum()
        st.bar_chart(chart_data)
    else:
        st.warning("No data found for selected filters")

# --------- Run ---------
execution()


