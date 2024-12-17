import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Noticias Relevantes", layout="wide")

# Cargar el archivo CSV
df = pd.read_csv("data/estructura_final.csv")  # Ajusta la ruta a tu archivo CSV

# Título principal
st.subheader("📰 Noticias Relevantes")

# Mostrar las noticias en formato similar a la imagen
for index, row in df.iterrows():
    col1, col2 = st.columns([1, 2])  # Define columnas, más espacio para texto
    
    # Columna 1: Imagen
    with col1:
        if pd.notnull(row["image"]):  # Verifica si hay una imagen
            st.image(row["image"], use_container_width =True)
        else:
            st.image("https://via.placeholder.com/150", use_container_width =True)  # Imagen por defecto
    
    # Columna 2: Título y descripción
    with col2:
        st.markdown(f"### {row['title']}")  # Título en grande
        st.write(row["description"])  # Descripción
        
        # Enlace para leer más
        st.markdown(
            f'<a href="{row["url"]}" target="_blank" style="color: #0063c9; font-weight: bold;">Leer más →</a>',
            unsafe_allow_html=True
        )

    # Línea divisoria entre noticias
    st.markdown("---")
