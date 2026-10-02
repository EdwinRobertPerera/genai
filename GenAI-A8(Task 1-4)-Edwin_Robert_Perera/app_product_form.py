import streamlit as st


st.title("Product Form")

product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox(
    "Category", ["Electronics", "Clothing", "Groceries", "Home & Kitchen", "Books"]
)
price = st.sidebar.number_input("Price", min_value=0.0, value=0.0, step=1.0)

if st.sidebar.button("Add Product"):
    if product_name.strip():
        st.success("Product added successfully!")
        st.write(f"**Product Name:** {product_name.strip()}")
        st.write(f"**Category:** {category}")
        st.write(f"**Price:** {price:.2f}")
    else:
        st.warning("Please enter a product name.")
