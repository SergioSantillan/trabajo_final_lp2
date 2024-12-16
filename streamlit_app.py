import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Noticias Tecnológicas", layout="wide")

# Barra lateral con el logo y título
st.sidebar.image("imagenes/tu_logo.png", use_container_width=True)  # Reemplaza con tu logo
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 24px; font-family: 'Georgia'; font-weight: bold; color: #2C3E50; margin-top: 15px;">
        Plataforma de Noticias Tecnológicas
    </div>
    """,
    unsafe_allow_html=True,
)

# Menú de la barra lateral
menu = st.sidebar.radio(
    "Menú Principal",
    ["Noticias Relevantes", "Selector de Noticias", "Conclusiones", "Miembros"]
)

# Sección de Noticias Relevantes
if menu == "Noticias Relevantes":
    st.title("📰 Noticias Relevantes")
    st.write("Aquí puedes introducir una descripción general o destacadas de las noticias más relevantes.")
    # Ejemplo de una noticia destacada
    st.subheader("Ejemplo de Noticia Destacada")
    st.write("Esta sección puede contener un resumen de las noticias más importantes o tendencias.")

# Sección de Selector de Noticias
elif menu == "Selector de Noticias":
    st.title("📊 Selector de Noticias")
    st.write("Filtra y visualiza noticias por temas específicos.")
    # Espacio para agregar el código del selector y la visualización de noticias
    st.write("Aquí puedes agregar botones o selectores para filtrar noticias por temas como AI, Apple, Tech, Business, etc.")

# Sección de Conclusiones
elif menu == "Conclusiones":
    st.title("📈 Conclusiones")
    st.write("Resumen y conclusiones derivadas del análisis de la base de datos de noticias.")
    # Espacio para agregar gráficos y conclusiones
    st.write("Aquí puedes mostrar gráficos y visualizaciones que resuman los hallazgos más importantes.")

# Sección de Miembros
elif menu == "Miembros":
    st.title("👥 Miembros del Equipo")
    st.write("""
    - **Nombre 1**: Descripción del rol o responsabilidad.
    - **Nombre 2**: Descripción del rol o responsabilidad.
    - **Nombre 3**: Descripción del rol o responsabilidad.
    """)
    # Espacio para agregar información adicional del equipo
    st.write("Esta sección puede contener información detallada sobre los miembros del equipo y sus contribuciones.")
