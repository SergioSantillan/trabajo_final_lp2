import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import math  # Para calcular el número de páginas

# Configuración de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Cargar el archivo CSV
df = pd.read_csv("data/estructura_solo_image.csv")  # Asegúrate de ajustar la ruta correcta

# Barra lateral con logo y menú
with st.sidebar:
    # Logo en la barra lateral
    st.image("imagenes/logo.png", use_container_width=True)

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
    
    # Parámetros de paginación
    NEWS_PER_PAGE = 15  # Número de noticias por página
    total_news = len(df)  # Total de noticias
    total_pages = math.ceil(total_news / NEWS_PER_PAGE)  # Calcula el total de páginas

    # Selección de página actual solo en la parte inferior
    page_number = st.session_state.get("page_number", 1)  # Usamos session_state para persistir la página actual

    # Índices para filtrar noticias por página
    start_idx = (page_number - 1) * NEWS_PER_PAGE
    end_idx = start_idx + NEWS_PER_PAGE
    current_page_news = df.iloc[start_idx:end_idx]

    # Mostrar las noticias en formato de columnas (imagen + texto)
    for index, row in current_page_news.iterrows():
        col1, col2 = st.columns([1, 2])  # Divide la fila en dos columnas

        # Columna 1: Imagen
        with col1:
            if pd.notnull(row["image"]):  # Verifica si hay imagen
                st.image(row["image"], use_container_width=True)
            else:
                st.image("https://via.placeholder.com/150", use_container_width=True)  # Imagen por defecto

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

    # Navegación con paginación en números
    st.write("### Páginas:")
    page_numbers = [i for i in range(1, total_pages + 1)]
    st.write(
        " ".join(
            f'<a style="color: #0063c9; font-weight: bold;" href="?page={p}">{p}</a>' 
            if p != page_number else f"<b>{p}</b>" 
            for p in page_numbers
        ),
        unsafe_allow_html=True
    )

    # Actualiza el número de página con los botones
    page_number = st.selectbox('Selecciona página', range(1, total_pages + 1), key="page_number")
    
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
