import streamlit as st


st.title("Simple Sales Dashboard")
st.write("View monthly sales and compare the results across four months.")

months = ["January", "February", "March", "April"]
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000,
}

selected_month = st.selectbox("Select a month", months)
st.metric(f"{selected_month} Sales", sales[selected_month])

st.subheader("Monthly Sales")
st.bar_chart(list(sales.values()))
