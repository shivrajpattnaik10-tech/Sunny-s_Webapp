import streamlit as st
import pandas as pd
from wordcloud import WordCloud

try:
    excel_file_path="/workspaces/codespaces-blank/data/expense.csv"
    def execution():
        dataframe=pd.read_csv(excel_file_path)
        if len(dataframe)!=0:
            dataframe["Date"]=pd.to_datetime(dataframe["Date"])
            min_Amount=dataframe[dataframe["Amount"]==dataframe["Amount"].max()]
            max_Amount=dataframe[dataframe["Amount"]==dataframe["Amount"].min()]
            st.subheader("You are spending the most here:cry:")
            st.dataframe(max_Amount.reset_index(drop=True))
            st.subheader("You are spending the least here:blush:")
            st.dataframe(max_Amount.reset_index(drop=True))
            st.subheader("You made the most number of transcations on:date:")
            most_txn=dataframe.groupby("Date").size().nlargest(1)
            st.dataframe(most_txn.reset_index(name="Count"))
            st.dataframe(dataframe.groupby(by="Date").size().nsmallest(1).index)
            least_txn=dataframe.groupby("Date").size().nlargest(1)
            st.subheader("You made the least number of transcations on:date:")
            mode_Category=dataframe["Category"].mode()
            st.subheader("The category for which you are spending the most:cry:")
            st.dataframe(mode_Category.reset_index(drop=True))
            st.subheader("The category for which you are spending the least:blush:")
            least_category=dataframe["Category"].value_counts().idxmin()
            st.dataframe(dataframe[dataframe["Category"].value_counts().idxmin()==dataframe["Category"]]["Category"].reset_index(drop=True))
            st.dataframe(pd.Dataframe([least_category],columns=["Category"]))
            Description_data=''.join(dataframe["Description"].astype(str).Values)
            wordcloud=WordCloud(width=400,height=400, background_clolr="white").generate(Description_data)
            st.subheader("Description Cloud")
            st.image(wordcloud.to_array())
            st.subheader("Category-wise spending")
            chart_data=dataframe.groupby("Category")["Amount"].sum()
            st.bar_chart(chart_data)
        else:
            st.header("Please add some expenses before analyzing it")
    execution()
except Exception as e:
    st.header("Please add some expenses before analyzing it")
