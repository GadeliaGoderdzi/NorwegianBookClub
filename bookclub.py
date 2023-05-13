import streamlit as st
import pandas as pd
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

df1 = pd.DataFrame(author)
df2 = pd.DataFrame(name)

with cluber:
    author = st.dataframe(df1)
    book = st.dataframe(df2)