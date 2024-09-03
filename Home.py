import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
         "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
         "when an unknown printer took a galley of type and scrambled it to make a type specimen book.")

st.header("Out Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv', sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']}  {row['last name']}".title())
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name']}  {row['last name']}".title())
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name']}  {row['last name']}".title())
        st.write(row['role'])
        st.image('images/' + row['image'])
