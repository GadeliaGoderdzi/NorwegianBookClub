import streamlit as st
#----------------------------------text editing------------------------------------
club = open("Norwegian Book Club 100.csv")
author = []
name = []

for book in club:
    book = book.split("by")
    st.write(book)
    author.append(book[1])
    name.append(book[0])

st.wrtite(author)
st.wrtite(name)