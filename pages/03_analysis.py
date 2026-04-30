import streamlit as st
import pandas as pd
import os
from wordcloud import WordCloud

# --------- File Path ---------
excel_file_path = "data/expense.csv"

def execution():
    # Ensure file exists
    if not os.path.exists(excel_file_path):
        st.warning("Please add some expenses before analyzing it")
        return

    dataframe = pd.read_csv(excel_file_path)

    if dataframe.empty:
        st.warning("Please add some expenses before analyzing it")
        return

    # --------- Date conversion ---------
    dataframe["Date"] = pd.to_datetime(dataframe["Date"], errors="coerce")
    dataframe = dataframe.dropna(subset=["Date"])

    # --------- Max & Min Spending ---------
    max_amount_df = dataframe[dataframe["Amount"] == dataframe["Amount"].max()]
    min_amount_df = dataframe[dataframe["Amount"] == dataframe["Amount"].min()]

    st.subheader("You are spending the most here 😢")
    st.dataframe(max_amount_df.reset_index(drop=True))

    st.subheader("You are spending the least here 😊")
    st.dataframe(min_amount_df.reset_index(drop=True))

    # --------- Transactions ---------
    txn_count = dataframe.groupby("Date").size()

    st.subheader("Most transactions on 📅")
    st.dataframe(txn_count.nlargest(1).reset_index(name="Count"))

    st.subheader("Least transactions on 📅")
    st.dataframe(txn_count.nsmallest(1).reset_index(name="Count"))

    # --------- Category Analysis ---------
    mode_category = dataframe["Category"].mode()

    st.subheader("Most spent category 😢")
    st.dataframe(mode_category.reset_index(drop=True))

    least_category = dataframe["Category"].value_counts().idxmin()

    st.subheader("Least spent category 😊")
    st.write(least_category)

    # --------- WordCloud ---------
    description_data = ' '.join(dataframe["Description"].astype(str).values)

    wordcloud = WordCloud(width=400, height=400, background_color="white").generate(description_data)

    st.subheader("Description Cloud ☁️")
    st.image(wordcloud.to_array())

    # --------- Chart ---------
    st.subheader("Category-wise spending 📊")
    chart_data = dataframe.groupby("Category")["Amount"].sum()
    st.bar_chart(chart_data)

# --------- Run ---------
execution()


