import streamlit as st
#----------------------------------text editing------------------------------------
club = open("Norwegian Book Club 100.csv")
author = []
name = []
cluber = st.container()
list_files = []
for book in club:
    list_files.append(book)
for book in list_files[1:]:
    book = book.split("by")
    author.append(book[1])
    name.append(book[0])

with cluber:
    st.write(list_files)
    st.write(author)
    st.write(name)