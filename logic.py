import pandas as pd

def hesapla_kar(menu_df, satis_df):
    """
    Menü ve satış verilerinden toplam kârı hesaplar.
    """
    # Menü verilerini ürün adına göre eşleştirme
    birlesik = satis_df.merge(menu_df, on="Ürün", how="left")
    
    # Satış başına maliyet ve gelir hesaplama
    birlesik["Toplam Maliyet"] = birlesik["Maliyet"] * birlesik["Adet"]
    birlesik["Toplam Gelir"] = birlesik["Fiyat"] * birlesik["Adet"]
    birlesik["Kâr"] = birlesik["Toplam Gelir"] - birlesik["Toplam Maliyet"]

    toplam_kar = birlesik["Kâr"].sum()
    return birlesik, toplam_kar
