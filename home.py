import streamlit as st
tab1,tab2,tab3=st.tabs(["About","Hobbies","Contact"])
with tab1:
    col1,col2=st.columns([0.4,0.7])
    with col1:
        st.image("Pictureofme.jpg",width=1000000)
        st.subheader("Sunny Pattnaik:sunglasses:")
    with col2:
        st.write("Hello, I am learning about creating web pages.")
with tab2:
    st.write("My hobbies are swimming and coding")
with tab3:
    st.write("Email: Shivrajpattnaik10@gmail.com")
    st.write("Website: https://sturdy-waddle-7vqj6vv795pvhw5v9-8501.app.github.dev/")
