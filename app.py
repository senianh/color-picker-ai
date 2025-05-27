# Nama Program    : app.py
# Nama            : Senia Nur Hasanah 
# NPM             : 140810230021 
# Tanggal Buat    : 27 Mei 2025 
# Deskripsi       : Program color picker berdasarkan warna dominan
                    

import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(page_title="Color Palette Extractor", layout="centered")

st.title("🎨 Color Palette Extractor")
st.write("Unggah gambar dan dapatkan 5 warna dominan dalam bentuk palet warna.")

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Gambar yang diunggah', use_container_width=True)

    # Ekstrak warna dominan
    img_array = np.array(image)
    pixels = img_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    # Tampilkan palet warna
    st.subheader("Palet Warna Dominan")
    fig, ax = plt.subplots(1, figsize=(8, 2))
    for i, color in enumerate(dominant_colors):
        r, g, b = color
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=np.array(color)/255))
        ax.text(i + 0.5, -0.3, f'RGB({r}, {g}, {b})', ha='center', va='top', fontsize=9)

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.axis('off')
    st.pyplot(fig)
