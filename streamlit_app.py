import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="My First Dashboard", layout="wide")
st.title("Selamat! Dashboard pertamaku sudah live")

df = pd.DataFrame ({
  "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
  "Pendapatan Data Science (M)":[1, 5, 8, 10, 50, 75],
  "Profit Investasi (M)": [100, 400, 560, 600, 700, 900]
})

col1, col2 = st.columns(2)
col1.metric("Total Pendapatan dari Data Science ", "Rp 2.5 Milyar", "+126%")
col2.metric("Total Profit Investasi S&P 500 & Crypto", "Rp 150 Milyar", "+900%")

fig = px.line (df, x = "Bulan", y= ["Penjualan (jt)", "Profit(jt)"],
               title= "Trend 6 Bulan Terakhir")
st.plotly_chart(fig, use_container_width=True)
st.success("Dashboard berhasil di-deploy! KAMU HEBAT STEVEN")
