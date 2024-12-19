import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import math  # Para calcular el número de páginas
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Cargar el archivo CSV
df = pd.read_csv("data/estructura_definitiva.csv")  # Asegúrate de ajustar la ruta correcta

# Barra lateral con logo y menú
with st.sidebar:
    st.image("imagenes/logo.png", use_container_width=True)

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
        menu_title="Menú Principal",
        options=["Selector de Noticias", "Gráficos Interactivos", "Conclusiones del Proyecto", "Miembros del Proyecto"],
        icons=["newspaper", "filter", "bar-chart", "people"],
        menu_icon="cast",
        default_index=0,
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

    # Campo de búsqueda para filtrar por palabras clave en la descripción
    search_query = st.text_input("🔍 Busca en las descripciones:", "")

    # Filtrar el DataFrame por la categoría seleccionada y búsqueda
    filtered_df = df

    if selected_category:
        filtered_df = filtered_df[filtered_df["category"].str.contains(selected_category, case=False, na=False)]

    if search_query:
        filtered_df = filtered_df[filtered_df["description"].str.contains(search_query, case=False, na=False)]

    # Parámetros de paginación
    NEWS_PER_PAGE = 15
    total_news = len(filtered_df)
    total_pages = max(1, math.ceil(total_news / NEWS_PER_PAGE))

    # Selección de página actual usando session_state
    page_number = st.session_state.get("page_number", 1)

    # Índices para filtrar noticias por página
    start_idx = (page_number - 1) * NEWS_PER_PAGE
    end_idx = start_idx + NEWS_PER_PAGE
    current_page_news = filtered_df.iloc[start_idx:end_idx]

    # Mostrar las noticias en formato de columnas (imagen + texto)
    for index, row in current_page_news.iterrows():
        col1, col2 = st.columns([1, 2])

        with col1:
            if pd.notnull(row["image"]):
                st.image(row["image"], use_container_width=True)
            else:
                st.image("https://via.placeholder.com/150", use_container_width=True)

        with col2:
            st.markdown(f"### {row['title']}")
            st.write(row["description"])

            st.markdown(
                f'<a href="{row["url"]}" target="_blank" style="color: #0063c9; font-weight: bold;">Leer más →</a>',
                unsafe_allow_html=True
            )

        st.markdown("---")

    # Navegación con el botón desplegable para elegir la página
    st.write("### Selecciona la página:")
    page_number = st.selectbox(
        'Elige la página', 
        range(1, total_pages + 1), 
        key="page_number", 
        index=page_number - 1
    )

elif menu == "Gráficos Interactivos":
    st.subheader("Gráficos Interactivos")
    st.write("Explora los gráficos generados a partir de las noticias.")

    # Gráfico 1: Top 5 categorías con más noticias
    top_categories = df['category'].value_counts().reset_index()
    top_categories.columns = ['Category', 'Count']

    custom_colors = ['#4e85d5', '#25a146', '#f8fb14', '#e51313', '#e26ec4']

    fig1 = px.bar(top_categories.head(5), x='Category', y='Count', text='Count')

    fig1.update_traces(marker_color=custom_colors[:len(top_categories.head(5))], textfont_size=14, textposition='outside')

    fig1.update_layout(
        title="<b>Top 5 Categorías con Más Noticias</b>",
        font=dict(family="Arial, sans-serif", size=16, color="#2c3e50"),
        template="plotly_white",
        plot_bgcolor="#FAFAFA",
        paper_bgcolor="#FFFFFF",
        yaxis=dict(showgrid=False),
        xaxis=dict(title=dict(font=dict(size=16, color="black"))),
        showlegend=False
    )

    st.plotly_chart(fig1)

    # Gráfico 2: Distribución de noticias por categoría
    category_counts = df['category'].value_counts()

    fig2 = px.pie(names=category_counts.index, values=category_counts.values, hole=0.3, 
                 color=category_counts.index, color_discrete_sequence=custom_colors)

    fig2.update_traces(
        textinfo='percent+label',
        pull=[0.1] * len(category_counts),
        textfont=dict(size=14, color='white'),
        marker=dict(line=dict(color='#FFFFFF', width=1))
    )

    fig2.update_layout(
        title="<b>Distribución de Noticias por Categoría</b>",
        title_font=dict(size=20, color='#333333'),
        font=dict(family="Arial, sans-serif", size=14, color="#333333"),
        template="plotly_white",
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#F4F4F4",
        showlegend=True
    )

    st.plotly_chart(fig2)

elif menu == "Miembros del Proyecto":
    st.subheader("👥 Miembros del Proyecto")
    st.write(""" 
    - **Miembro 1**: Analista de datos  
    - **Miembro 2**: Especialista en visualización  
    - **Miembro 3**: Ingeniero en IA  
    - **Miembro 4**: Desarrollador web  
    """)
