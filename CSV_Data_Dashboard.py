

import streamlit as st
import pandas as pd
st.title("My First CSV")
file= st.file_uploader("Upload CSV file",type=["csv"])
if file is not None:
     st.write("Data Preview")
     df= pd.read_csv(file)
     st.dataframe(df)
     st.write("Summary")
     st.write(df.describe())
     st.bar_chart(df.select_dtypes(include='number'))
     
	