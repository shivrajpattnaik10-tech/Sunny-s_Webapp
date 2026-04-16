import streamlit as st
import pandas as pd

# File path
excel_file_path = "/workspaces/codespaces-blank/data/expense.csv"

def execution():
    # Load data
    dataframe = pd.read_csv(excel_file_path)

    # Convert Date column safely
    dataframe["Date"] = pd.to_datetime(dataframe["Date"], errors='coerce')

    # Remove invalid dates
    dataframe = dataframe.dropna(subset=["Date"])

    # Stop if no valid data
    if dataframe.empty:
        st.error("No valid data found in CSV")
        return

    # Total calculation
    total = dataframe["Amount"].sum()
    st.subheader(f"Gold coins: {int(total)//200} 🪙")

    # Date filters (safe now)
    date_from = st.date_input("From Date 📅", dataframe["Date"].min())
    date_to = st.date_input("To Date 📅", dataframe["Date"].max())

    # Amount filters
    amount_min = st.slider("Minimum value", 0, 20000, 0, 10)
    amount_max = st.slider("Maximum value", 0, 20000, 20000, 10)

    # Category filter
    category = st.multiselect(
        "Categories 🗂️",
        ["Housing","Utilities","Transportation","Food","Healthcare","Insurance",
         "Debt Payments","Entertainment","Personal Care","Education",
         "Savings","Taxes","Miscellaneous"]
    )

    # Apply filters
    filtered_df = dataframe[
        (dataframe["Date"] >= pd.to_datetime(date_from)) &
        (dataframe["Date"] <= pd.to_datetime(date_to)) &
        (dataframe["Amount"] >= amount_min) &
        (dataframe["Amount"] <= amount_max)
    ]

    # Apply category filter if selected
    if category:
        filtered_df = filtered_df[filtered_df["Category"].isin(category)]

    # Show filtered data
    st.dataframe(filtered_df)

    # Show chart
    if not filtered_df.empty:
        chart_data = filtered_df.groupby("Category")["Amount"].sum()
        st.bar_chart(chart_data)
    else:
        st.warning("No data found for selected filters")

# Run function
execution()