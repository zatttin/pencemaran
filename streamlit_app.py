import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="Web Apps", page_icon=":blue[Menilai Tingkat Pencemaran Air Limbah]")

# Create a header section
st.write("Aplikasi ini dibuat oleh kelompok 8 kelas PLI")

st.title("SELAMAT DATANG DI WEB APPS MENILAI TINGKAT PENCEMARAN AIR LIMBAH")

st.markdown("<h1 style='color: black'>Web Apps Menentukan Indeks Kualitas Air Limbah Menggunakan Metode Storet</h1>", unsafe_allow_html=True)

# Membuat Sidebar
with st.sidebar:
    selected_tab = st.selectbox("Pilih Tab", ["Perkenalan", "Metode Storet", "Baku Mutu Air Limbah"])

# Tab: Perkenalan
if selected_tab == "Perkenalan":
    st.header("Pencemaran Air")
    st.markdown("<style>h2{color: #3e8e41;}</style>", unsafe_allow_html=True)
    st.write("Pencemaran Air adalah masuk atau dimasukkannya mahluk hidup, zat, energi, dan atau komponen lain kedalam air oleh kegiatan manusia, sehingga melampaui mutu lingkungan hidup yang telah ditetapkan.")   
    st.header("Indeks kualitas air (IKA) ")
    st.write("Indeks kualitas air (IKA) memberikan nilai tunggal yang mengekspresikan keseluruhan kualitas air pada lokasi dan waktu tertentu berdasarkan beberapa parameter kualitas air.  ")

    st.header("Metode Storet")
    st.write("Metode Storet merupakan cara untuk menentukan status mutu air dengan menggunakan sistem nilai dari “US-EPA (Environmental Protection Agency)” dengan mengklasifikasikan mutu air dalam empat kelas, yaitu:")

    st.header("Cara Penggunaan Aplikasi ")
    st.write("- Untuk menggunakan aplikasi, silahkan tekan tombol > pada bagian kiri atas.")
    st.write("- Untuk menentukan IKA menggunakan cara storet silahkan pilih menu Metode Storet")
    st.write("- Untuk melihat baku mutu silahkan pilih menu Baku Mutu Air Limbah")

# Tab 1: Storet Calculation
elif selected_tab == "Metode Storet":
    st.title("Penentuan Indeks Kualitas Air")
    st.write('Perhitungan status mutu air dalam aplikasi ini ditentukan menggunakan metode storet.')
    
    st.write("Silahkan masukkan data pengujian untuk menentukan skor status mutu air.")
    st.write("Pastikan data yang dimasukkan sudah benar")

    # Memasukkan Kadar dan Baku Mutu
    konsentrasi = st.number_input("Konsentrasi Pengujian (mg/L)", min_value=0.0)
    
    # Selectbox for Baku Mutu
    baku_mutu_options = ["BOD", "COD", "TSS", "Minyak Lemak", "Besi Terlarut (Fe)", "Mangan Terlarut(Mn)", 
                         "Barium (Ba)", "Tembaga (Cu)", "Seng (Zn)", "Krom Heksavalen(Cr⁶)",
                         "Krom Total (Cr)", "Cadmium (Cd)", "Air Raksa (Hg)", "Timbal (Pb)",
                         "Stanum (Sn)", "Arsen (As)", "Selenium (Se)", "Nikel (Ni)", "Kobalt (Co)",
                         "Sianida (CN)", "Sulfida (H2S)", "Fluorida (F)", "Klorin Bebas (Cl2)",
                         "Amonia-Nitrogen (NH3-N)", "Nitrat (NO3-N)", "Nitrit (NO2-N)",
                         "Total Nitrogen", "Senyawa aktif biru metilen", "Fenol"]
    
    baku_mutu_selected = st.selectbox("Pilih Baku Mutu", baku_mutu_options)

    # Map Baku Mutu to actual value
    baku_mutu = {
        "BOD": 50,
        "COD": 100,
        "TSS": 200,
        "Minyak Lemak": 10,
        "Besi Terlarut (Fe)": 4,
        "Mangan Terlarut (Mn)": 2,
        "Barium (Ba)": 2,
        "Tembaga (Cu)": 2,
        "Seng (Zn)": 5,
        "Krom Heksavalen(Cr⁶)": 0.1,
        "Krom Total (Cr)": 0.5,
        "Cadmium (Cd)": 0.05,
        "Air Raksa (Hg)": 0.002,
        "Timbal (Pb)": 0.1,
        "Stanum (Sn)": 2,
        "Arsen (As)": 0.1,
        "Selenium (Se)": 0.05,
        "Nikel (Ni)": 0.2,
        "Kobalt (Co)": 0.4,
        "Sianida (CN)": 0.05,
        "Sulfida (H2S)": 0.5,
        "Fluorida (F)": 2,
        "Klorin Bebas (Cl2)": 1,
        "Amonia-Nitrogen (NH3-N)": 5,
        "Nitrat (NO3-N)": 20,
        "Nitrit (NO2-N)": 1,
        "Total Nitrogen": 30,
        "Senyawa aktif biru metilen": 5,
        "Fenol": 0.5
    }

    # Calculate Storet score
    def hitung_skor_storet(konsentrasi, baku_mutu):
        selisih = konsentrasi - baku_mutu
        if selisih <= 0:
            return 0
        elif selisih <= baku_mutu * 0.25:
            return 1
        elif selisih <= baku_mutu * 0.5:
            return 3
        elif selisih <= baku_mutu * 0.75:
            return 6
        else:
            return 10  # added this to ensure skor can reach 10

    # Button to calculate Storet score
    if st.button("Hitung Skor Storet"):
        skor = hitung_skor_storet(konsentrasi, baku_mutu[baku_mutu_selected])
        st.write(f"Skor Storet: {skor}")

        # Determine pollution status
        if skor == 0:
            st.write("Status: Tidak Tercemar")
            st.write('Kelas A')
        elif skor <= 3:
            st.write("Status: Tercemar Ringan")
            st.write('Kelas B')
        elif skor <= 6:
            st.write("Status: Tercemar Sedang")
            st.write('Kelas C')
        else:
            st.write("Status: Tercemar Berat")
            st.write('Kelas D')

# Tab 2: Baku Mutu Air Limbah
elif selected_tab == "Baku Mutu Air Limbah":
    st.title("Baku Mutu Air Limbah")
    st.write("Berikut adalah tabel baku mutu air limbah yang dapat digunakan sebagai acuan.")
    st.write("Baku Mutu Berdasarkan Acuan Peraturan Menteri Lingkungan Hidup Nomor : 05 Tahun 2014 TENTANG BAKU MUTU AIR LIMBAH Lampiran XLVII")

    # Create a DataFrame for Baku Mutu Air Limbah
    baku_mutu_df = pd.DataFrame({
        'Parameter': ['BOD', 'COD', 'TSS', 'Minyak Lemak', 'Besi Terlarut (Fe)', 'Mangan Terlarut (Mn)', 
                       'Barium (Ba)', 'Tembaga (Cu)', 'Seng (Zn)', 'Krom Heksavalen(Cr⁶)', 
                       'Krom Total (Cr)', 'Cadmium (Cd)', 'Air Raksa (Hg)', 'Timbal (Pb)', 
                       'Stanum (Sn)', 'Arsen (As)', 'Selenium (Se)', 'Nikel (Ni)', 'Kobalt (Co)',
                       'Sianida (CN)', 'Sulfida (H2S)', 'Fluorida (F)', 'Klorin Bebas (Cl2)',
                       'Amonia-Nitrogen (NH3-N)', 'Nitrat (NO3-N)', 'Nitrit (NO2-N)',
                       'Total Nitrogen', 'Senyawa aktif biru metilen', 'Fenol'],
        'Baku Mutu Golongan I (mg/L)': [50, 100, 200, 10, 4, 2, 2, 2, 5, 0.1, 0.5, 0.05, 0.002, 0.1, 2, 0.1, 0.05, 0.2, 0.4,
                             0.05, 0.5, 2, 1, 5, 20, 1, 30, 5, 0.5]
    })

    # Display the DataFrame
    st.dataframe(baku_mutu_df)
s
