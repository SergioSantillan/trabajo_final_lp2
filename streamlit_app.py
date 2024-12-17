import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Cargar el archivo CSV
df = pd.read_csv("data/estructura_final.csv")  # Asegúrate de ajustar la ruta correcta

# Barra lateral con logo y menú
with st.sidebar:
    # Logo en la barra lateral
    st.image("imagenes/logo.png", use_container_width =True)

    # Título estilizado en la barra lateral
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; font-family: 'Georgia'; font-weight: bold; color: #0063c9; margin-top: 15px;">
            Plataforma de Noticias
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Menú de navegación en la barra lateral
    menu = option_menu(
        menu_title="Menú Principal",  # Título del menú
        options=["Noticias Relevantes", "Selector de Noticias", "Gráficos Interactivos", "Miembros del Proyecto"],  # Opciones
        icons=["newspaper", "filter", "bar-chart", "people"],  # Íconos de cada opción
        menu_icon="cast",  # Ícono principal del menú
        default_index=0,  # Primera opción seleccionada por defecto
        orientation="vertical",
    )

# Contenido dinámico basado en el menú seleccionado
if menu == "Noticias Relevantes":
    st.subheader("📰 Noticias Relevantes")
    
    # Mostrar las noticias en formato de columnas (imagen + texto)
    for index, row in df.iterrows():
        col1, col2 = st.columns([1, 2])  # Divide la fila en dos columnas
        
        # Columna 1: Imagen
        with col1:
            if pd.notnull(row["image"]):  # Verifica si hay imagen
                st.image(row["image"], use_container_width =True)
            else:
                st.image("https://via.placeholder.com/150", use_container_width =True)  # Imagen por defecto
        
        # Columna 2: Título y descripción
        with col2:
            st.markdown(f"### {row['title']}")  # Título de la noticia
            st.write(row["description"])  # Descripción de la noticia
            
            # Enlace estilizado
            st.markdown(
                f'<a href="{row["url"]}" target="_blank" style="color: #0063c9; font-weight: bold;">Leer más →</a>',
                unsafe_allow_html=True
            )
        
        # Línea divisoria entre noticias
        st.markdown("---")

elif menu == "Selector de Noticias":
    st.subheader("🔍 Selector de Noticias")
    st.write("Filtra y selecciona las noticias que te interesen.")

elif menu == "Gráficos Interactivos":
    st.subheader("📊 Gráficos Interactivos")
    st.write("Explora los gráficos generados a partir de las noticias.")

elif menu == "Miembros del Proyecto":
    st.subheader("👥 Miembros del Proyecto")
    st.write("""
    - **Miembro 1**: Analista de datos  
    - **Miembro 2**: Especialista en visualización  
    - **Miembro 3**: Ingeniero en IA  
    - **Miembro 4**: Desarrollador web  
    """)
