import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
###

st.title("Excel file ")
st.write("This is a summury of excel file.")
# Create 4 columns
# col1, col2, col3, col4 = st.columns(4)

# # Add content to each column
# col1.write("Data review ")
# col2.write("Data stat")
# col3.write("Data columns")
# col4.write("Column 4")


######## Part two
# File Uploader in Sidebar
uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx", "xls"])

# Image Uploader in Sidebar
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# Define page navigation
page = st.sidebar.radio("Choose a page", ["Home", "Preview", "Summary", "Column Names", "Shape", "Graphics"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    if page == "Home":
        st.title("Welcome! Choose an option from the sidebar.")

    elif page == "Preview":
        st.title("Data Preview")
        st.dataframe(df.head(5))  # Show first 5 rows

    elif page == "Summary":
        st.title("Summary Statistics")
        st.write(df.describe())  # Show summary stats

    elif page == "Column Names":
        st.title("Column Names")
        st.write(df.columns)  # Show column names

    elif page == "Shape":
        st.title("Dataset Shape")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")  # Show dimensions

    elif page == "Graphics":
        st.title("Data Visualization")
        
        # Let user select columns for plot
        selected_columns = st.multiselect("Select Columns for Plot", df.columns.tolist())
        
        if len(selected_columns) > 1:
            st.write(f"Plotting {', '.join(selected_columns)}")
            sns.pairplot(df[selected_columns])
            st.pyplot()  # Display the plot

        else:
            st.warning("Please select at least two columns for a plot.")

else:
    st.title("Upload an Excel file to display data.")

# Display uploaded image (if any)
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)






















































# # Main Page - Split into 4 Columns
# col1, col2, col3, col4 = st.columns(4)

# if upload_file is not None:
#     df = pd.read_excel(upload_file)

#     # Display Data in Columns
#     col1.write("Column 1 - Preview")
#     col1.dataframe(df.head(5))  # Show first 5 rows

#     col2.write("Column 2 - Summary")
#     col2.write(df.describe())  # Show summary stats

#     col3.write("Column 3 - Column Names")
#     col3.write(df.columns)  # Show column names

#     col4.write("Column 4 - Shape")
#     col4.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")  # Show dimensions

# else:
#     st.write("Upload an Excel file to display data.")