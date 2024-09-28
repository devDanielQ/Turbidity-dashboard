import os
import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="Turdbidity Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")
# Page Title
UG_logo = r"C:\Users\Fadere\Desktop\Daniel\Work Folder\GMES_Phase2\Partner_logos\UG_Logo_1.png"
st.title("Turbidity Monitoring Dashboard")
st.divider()

# Adding logo
st.logo(UG_logo, link=None, icon_image=None)

# Sidebar
with st.sidebar:
    #st.sidebar.image(UG_logo, use_column_width=True)
    st.sidebar.header("About App")
    st.sidebar.write("Ahw3nsuo is an app developed to display the levels of turbidity in tanks at home")
    # Add Feedback section at the bottom of the sidebar
    st.sidebar.subheader("Feedback")

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

# Load Data
data_dir = r"C:\Users\Fadere\Downloads\turbidity"
os.chdir(data_dir)
files = os.listdir(data_dir)
file = files[-1]
df = pd.read_csv(os.path.join(data_dir, file))

# Data Preview Expandet
with st.expander("Data Preview"):
    st.dataframe(df)

# Calculate minimum and maximum turbidity
min_turbidity = df['Turbidity'].min()
max_turbidity = df['Turbidity'].max()
mean_turbidity = df['Turbidity'].mean()

# WHO Turbidity Standard (e.g., 5 NTU for drinking water)
WHO_TURBIDITY_STANDARD = 5

# Display metrics
st.subheader("Turbidity Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Minimum Turbidity", value=min_turbidity)
with col2:
    st.metric(label="Maximum Turbidity", value=max_turbidity)
with col3:
    st.metric(label="Mean Turbidity", value=round(mean_turbidity, 2))

# Comparison with WHO standard
if mean_turbidity <= WHO_TURBIDITY_STANDARD:
    color = "green"
    message = f"Water meets WHO standard (≤ {WHO_TURBIDITY_STANDARD} NTU and it is safe to use)"
else:
    color = "red"
    message = f"Water exceeds WHO standard (> {WHO_TURBIDITY_STANDARD} NTU and it is unsafe to use)"

# Display WHO standard comparison result with color
st.markdown(f"<h4 style='color:{color};'>{message}</h4>", unsafe_allow_html=True)

# Line chart
st.subheader("Turbidity Over Time")
st.line_chart(df, x="Time", y="Turbidity", color="#588157")

