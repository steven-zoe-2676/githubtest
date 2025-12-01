import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="My First Dashboard", layout="wide")
st.title("Selamat! Dashboard pertamaku sudah live")

df = pd.DataFrame ({
  "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
  "Penjualan (jt)":[120, 150, 180, 165, 200, 250],
  "Profit(jt)": [30, 45, 60, 50, 70, 90]
})

col1, col2 = st.columns(2)
col1.metric("Total Penjualan", "1.065 juta", "+25%")
col2.metric("Total Profit", "345 juta", "+38%")

fig = px.line (df, x = "Bulan", y= [Penjualann (jt)", Profit(jt)"],
               title= "Trend 6 Bulan Terakhir")
st.plotly_chart(fig, use_container_width=True)
st.success("Dashboard berhasil di-deploy! KAMU HEBAT STEVEN")
