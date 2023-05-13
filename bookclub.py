import streamlit as st
#----------------------------------text editing------------------------------------
club = open("Norwegian Book Club 100.csv")
author = []
name = []
cluber = st.container()
list_files = []
for book in club:
    list_files.append(book)
# for book in club:
#     book = book.split("by")
#     st.write(book)
#     author.append(book[1])
#     name.append(book[0])

with cluber:
    st.write(list_files)
    st.wrtite(author)
    st.wrtite(name)