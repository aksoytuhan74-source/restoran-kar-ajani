import streamlit as st
import pandas as pd
from logic import hesapla_kar

st.title("🍽️ Restoran Kâr Analiz Aracı")

st.write("Bu araç, menü ve satış verilerinizi kullanarak kârınızı hesaplar.")

# Menü dosyası yükleme
menu_file = st.file_uploader("Menü dosyasını yükle (CSV)", type=["csv"])
satis_file = st.file_uploader("Satış dosyasını yükle (CSV)", type=["csv"])

if menu_file and satis_file:
    menu_df = pd.read_csv(menu_file)
    satis_df = pd.read_csv(satis_file)

    st.subheader("📊 Menü Verileri")
    st.dataframe(menu_df)

    st.subheader("🛒 Satış Verileri")
    st.dataframe(satis_df)

    birlesik, toplam_kar = hesapla_kar(menu_df, satis_df)

    st.subheader("🔎 Hesaplama Sonuçları")
    st.dataframe(birlesik)

    st.success(f"💰 Toplam Kâr: {toplam_kar} TL")
else:
    st.info("Devam etmek için menü ve satış CSV dosyalarını yükleyin.")
