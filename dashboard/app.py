import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURASI UMUM ---
st.set_page_config(page_title="Dashboard Sepeda", layout="wide")

st.title("Aplikasi Visualisasi Peminjaman Sepeda 🚲")
st.write("Analisis interaktif data peminjaman sepeda berdasarkan musim dan waktu.")

# --- SIDEBAR UNTUK INTERAKSI ---
st.sidebar.header("Filter Visualisasi")
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim",
    options=["Dingin", "Gugur", "Panas", "Semi"],
    default=["Dingin", "Gugur", "Panas", "Semi"],
)
show_pie = st.sidebar.checkbox("Tampilkan Pie Chart Pengguna", value=True)
show_cuaca = st.sidebar.checkbox("Tampilkan Heatmap Cuaca", value=True)
show_libur = st.sidebar.checkbox("Tampilkan Data Hari Libur", value=True)
show_penguna = st.sidebar.checkbox("Tampilkan Data pengguna", value=True)

# --- DATA ---
data = {
    "season": ["Dingin", "Gugur", "Panas", "Semi"],
    "Malam": [267.46, 346.36, 299.77, 146.93],
    "Pagi": [59.00, 72.31, 56.83, 30.52],
    "Siang": [269.30, 288.73, 267.70, 151.71],
}
df = pd.DataFrame(data)
df = df[df["season"].isin(selected_seasons)]

# --- VISUALISASI: PEMINJAMAN PER MUSIM DAN BLOK WAKTU ---
st.subheader("Jumlah Peminjaman Sepeda per Musim dan Blok Waktu (8 Jam)")
fig, ax = plt.subplots(figsize=(10, 6))
df.set_index("season").plot(kind="bar", stacked=False, colormap="viridis", ax=ax)
plt.title("Jumlah Peminjaman Sepeda per Musim dan Blok Waktu (8 Jam)", fontsize=16)
plt.xlabel("Musim", fontsize=12)
plt.ylabel("Jumlah Peminjaman Sepeda", fontsize=12)
st.pyplot(fig)

# --- VISUALISASI: HEATMAP CUACA ---
if show_cuaca:
    st.subheader("Frekuensi Cuaca per Musim dan Blok Waktu (8 Jam)")
    cuaca_data = {
        "season": ["Dingin", "Gugur", "Panas", "Semi"],
        "Malam": [350, 254, 303, 339],
        "Pagi": [414, 336, 385, 417],
        "Siang": [484, 357, 456, 449],
    }
    cuaca_df = pd.DataFrame(cuaca_data)
    cuaca_df = cuaca_df[cuaca_df["season"].isin(selected_seasons)]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        cuaca_df.set_index("season"), annot=True, cmap="YlGnBu", fmt=".1f", ax=ax
    )
    st.pyplot(fig)

# --- VISUALISASI: PIE CHART PENGGUNA ---
if show_pie:
    st.subheader("Persentase Pengguna Casual dan Registered")
    persentase_data = {
        "Tipe Pengguna": ["Casual", "Registered"],
        "Persentase (%)": [18.83, 81.17],
    }
    persentase_df = pd.DataFrame(persentase_data)
    fig, ax = plt.subplots(figsize=(7, 7))
    plt.pie(
        persentase_df["Persentase (%)"],
        labels=persentase_df["Tipe Pengguna"],
        autopct="%1.2f%%",
        startangle=90,
        colors=["#ff9999", "#66b3ff"],
    )
    plt.title("Persentase Pengguna Casual dan Registered", fontsize=16)
    st.pyplot(fig)

# --- VISUALISASI: JUMLAH HARI LIBUR ---
if show_libur:
    st.subheader("Jumlah Hari Libur Nasional dan Akhir Pekan")
    libur_data = {
        "Tipe Libur": ["Libur Nasional (holiday)", "Akhir Pekan (Sabtu & Minggu)"],
        "Jumlah Hari": [21, 210],
    }
    libur_df = pd.DataFrame(libur_data)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x="Tipe Libur", y="Jumlah Hari", data=libur_df, palette="viridis")
    plt.title("Jumlah Hari Libur Nasional dan Akhir Pekan", fontsize=16)
    plt.xlabel("Tipe Libur", fontsize=12)
    plt.ylabel("Jumlah Hari", fontsize=12)
    st.pyplot(fig)

# --- VISUALISASI: PERBANDINGAN PENGGUNA DI HARI KERJA & AKHIR PEKAN ---
if show_penguna:
    st.subheader(
        "Perbandingan Pengguna Casual dan Registered antara Hari Kerja dan Akhir Pekan"
    )
    data_pengguna = {
        "Tipe Pengguna": ["Casual", "Registered"],
        "Hari Kerja": [606.57, 3978.25],
        "Akhir Pekan": [1371.13, 2959.03],
    }
    pengguna_df = pd.DataFrame(data_pengguna)
    fig, ax = plt.subplots(figsize=(10, 6))
    pengguna_df.set_index("Tipe Pengguna").plot(
        kind="bar", stacked=False, colormap="Set2", ax=ax
    )
    plt.title(
        "Perbandingan Pengguna Casual dan Registered antara Hari Kerja dan Akhir Pekan",
        fontsize=16,
    )
    plt.xlabel("Tipe Pengguna", fontsize=12)
    plt.ylabel("Jumlah Peminjaman Sepeda", fontsize=12)
    st.pyplot(fig)
