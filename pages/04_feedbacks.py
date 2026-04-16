import streamlit as st
import pandas as pd
import os

folder_path = "data"
excel_file_path = "data/feedbacks.csv"

# Create folder if not exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create file with headers if not exists OR empty
if not os.path.exists(excel_file_path) or os.stat(excel_file_path).st_size == 0:
    df = pd.DataFrame(columns=["Name", "Feedback", "Rating"])
    df.to_csv(excel_file_path, index=False)

# Clear function (FIXED)
def Clear():
    st.session_state["nam"] = ""
    st.session_state["fed"] = ""

# Inputs
name = st.text_input("Enter your name", key="nam")
feedback = st.text_input("Please provide your feedback", key="fed")
rating = st.slider("Please provide a rating on a scale of 1-5", 1, 5, 1)

# Emoji feedback
emoji_holder = st.empty()
if rating == 1:
    emoji_holder.subheader("We will definitely improve 😟")
elif rating == 2:
    emoji_holder.subheader("We will definitely improve your experience 😥")
elif rating == 3:
    emoji_holder.subheader("Thanks!! 😐")
elif rating == 4:
    emoji_holder.subheader("Oh you are loving it!! 😺")
elif rating == 5:
    emoji_holder.subheader("Thank you so much for your love!!! 😍")

# Buttons
col1, col2 = st.columns([0.2, 0.8])
with col1:
    submit = st.button("Submit 😊")
with col2:
    clear = st.button("Clear ✂️", on_click=Clear)

# Insert function (SAFE)
def insert():
    try:
        df = pd.read_csv(excel_file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["Name", "Feedback", "Rating"])

    df.loc[len(df)] = [name, feedback, rating]
    df.to_csv(excel_file_path, index=False)

# View function (SAFE)
def view():
    try:
        df = pd.read_csv(excel_file_path)
        st.dataframe(df)
    except pd.errors.EmptyDataError:
        st.warning("No feedback available yet.")

# Submit action
if submit:
    if name.strip() == "" or feedback.strip() == "":
        st.warning("Please fill all fields")
    else:
        insert()
        st.success("Thank you for your valuable feedback")

# Show data
st.subheader("Past feedbacks")
view()