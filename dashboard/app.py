import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
pembayaran = pd.read_csv(r"C:\Users\Lenovo\Documents\DBS CAMP\course\py\pembayaran.csv")
deskripsi_penjualan = pd.read_csv(
    r"C:\Users\Lenovo\Documents\DBS CAMP\course\py\deskripsi_penjualan.csv"
)

# Sidebar
st.sidebar.header("Dashboard Analisis Data")
st.sidebar.subheader("Filter Data")

# Pilihan Metode Pembayaran
metode_pilihan = st.sidebar.multiselect(
    "Pilih Metode Pembayaran",
    pembayaran["payment_type"].unique(),
    pembayaran["payment_type"].unique(),
)

# Filter Data
filtered_pembayaran = pembayaran[pembayaran["payment_type"].isin(metode_pilihan)]

# Judul Dashboard
st.title("Dashboard Analisis Data")

# 1. Ringkasan Data
st.header("Ringkasan Data")
st.write("Jumlah Transaksi:", len(pembayaran))
st.write("Total Pendapatan:", pembayaran["payment_value"].sum())

# 2. Distribusi Metode Pembayaran
st.header("Distribusi Metode Pembayaran")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(
    x="payment_type",
    data=filtered_pembayaran,
    palette="viridis",
    order=filtered_pembayaran["payment_type"].value_counts().index,
)
plt.xticks(rotation=45)
plt.xlabel("Metode Pembayaran")
plt.ylabel("Jumlah Transaksi")
plt.title("Jumlah Transaksi Berdasarkan Metode Pembayaran")
st.pyplot(fig)

# 3. Scatter Plot Panjang Deskripsi vs Total Penjualan
st.header("Hubungan Panjang Deskripsi Produk dengan Total Penjualan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    x=deskripsi_penjualan["product_description_lenght"],
    y=deskripsi_penjualan["price"],
    alpha=0.5,
)
plt.xlabel("Panjang Deskripsi Produk")
plt.ylabel("Total Penjualan")
plt.title("Scatter Plot: Panjang Deskripsi vs Total Penjualan")
st.pyplot(fig)

# 4. Boxplot Metode Pembayaran vs Nilai Transaksi
st.header("Distribusi Nilai Transaksi Berdasarkan Metode Pembayaran")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x="payment_type", y="payment_value", data=filtered_pembayaran)
plt.yscale("log")  # Menggunakan log scale untuk menangani outlier
plt.xlabel("Metode Pembayaran")
plt.ylabel("Nilai Transaksi (Log Scale)")
plt.title("Boxplot: Metode Pembayaran vs Nilai Transaksi")
st.pyplot(fig)
