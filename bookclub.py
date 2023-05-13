import streamlit as st
#----------------------------------text editing------------------------------------
club = open("Norwegian Book Club 100.csv")
author = []
name = []
cluber = st.container()

for book in club[1:]:
    book = book.split("by")
    st.write(book)
    author.append(book[1])
    name.append(book[0])

with cluber:
    st.wrtite(author)
    st.wrtite(name)