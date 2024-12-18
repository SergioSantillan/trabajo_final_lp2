import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import math  # Para calcular el número de páginas

# Configuración de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Cargar el archivo CSV
df = pd.read_csv("data/estructura_definitiva.csv")  # Asegúrate de ajustar la ruta correcta

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
        options=["Selector de Noticias", "Gráficos Interactivos", "Conclusiones del Proyecto", "Miembros del Proyecto"],  # Opciones
        icons=["newspaper", "filter", "bar-chart", "people"],  # Íconos de cada opción
        menu_icon="cast",  # Ícono principal del menú
        default_index=0,  # Primera opción seleccionada por defecto
        orientation="vertical",
    )

# Contenido dinámico basado en el menú seleccionado
if menu == "Selector de Noticias":
    
    # Botones para filtrar noticias por categoría
    st.write("### Filtra por categoría:")
    categories = ["TECH", "AI", "SOCIETY", "GAMING", "LIFESTYLE", "POLITICS", "CYBERSECURITY", "AUTOMOBILE"]

    # Crear una fila de botones para cada categoría
    col1, col2, col3, col4 = st.columns(4)

    # Diccionario para mapear botones a columnas
    category_buttons = {
        col1: categories[:2],
        col2: categories[2:4],
        col3: categories[4:6],
        col4: categories[6:]
    }

    # Estado para la categoría seleccionada
    selected_category = st.session_state.get("selected_category", None)

    # Renderizar botones y capturar la categoría seleccionada
    for col, cat_list in category_buttons.items():
        with col:
            for cat in cat_list:
                if st.button(cat):
                    selected_category = cat
                    st.session_state["selected_category"] = cat

    # Filtrar el DataFrame por la categoría seleccionada
    if selected_category:
        filtered_df = df[df["category"].str.contains(selected_category, case=False, na=False)]
    else:
        filtered_df = df

    # Parámetros de paginación
    NEWS_PER_PAGE = 15  # Número de noticias por página
    total_news = len(filtered_df)  # Total de noticias filtradas
    total_pages = max(1, math.ceil(total_news / NEWS_PER_PAGE))  # Calcula el total de páginas

    # Selección de página actual usando session_state
    page_number = st.session_state.get("page_number", 1)

    # Índices para filtrar noticias por página
    start_idx = (page_number - 1) * NEWS_PER_PAGE
    end_idx = start_idx + NEWS_PER_PAGE
    current_page_news = filtered_df.iloc[start_idx:end_idx]

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

    # Navegación con el botón desplegable para elegir la página
    st.write("### Selecciona la página:")
    page_number = st.selectbox(
        'Elige la página', 
        range(1, total_pages + 1), 
        key="page_number", 
        index=page_number - 1  # Inicia el selectbox con la página actual
    )

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
