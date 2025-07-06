import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("The Best Company")
content = """
Lorem ipsum is a dummy text used in the design and publishing industry, 
originating from a scrambled passage of Cicero's work from the 15th century. 
It serves as a placeholder text in graphic design, web development, and publishing 
to focus attention on design elements rather than content. 
"""
st.write(content)
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over rows 0 to 3
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the third column
with col3:
    # Iterate over rows 8 to 12
    for index, row in df[8:12].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])
