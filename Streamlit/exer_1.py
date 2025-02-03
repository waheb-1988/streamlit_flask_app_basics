import streamlit as st 
import pandas as pd

st.title(" First test 5 data")

# col1,col2,col3,col4 = st.columns(4)

# col1.write("test1")

# col2.write("test2")

# col3.write("test2")

# col4.write("test2")

st.sidebar.title('my first side bar')


path = st.sidebar.file_uploader("Upload_excel", type = ["xlsx"] )

if path is None :
    assert ("import file")
else :

    # st.dataframe(df_head)
    # df.describe()
    df = pd.read_excel(path)
    pages= st.sidebar.radio('Home', ["View","Stat desc"], index=None)

    if pages == "View":

        
        st.dataframe(df.head(5))
        
    elif  pages == "Stat desc":
        
        st.dataframe(df.describe())
