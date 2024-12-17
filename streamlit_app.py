import streamlit as st
from streamlit_option_menu import option_menu

# Configuración básica de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Colocar el logo en la barra lateral
st.sidebar.image("imagenes/logo.png", use_container_width=True)

# Título estilizado en la barra lateral
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 24px; font-family: 'Georgia'; font-weight: bold; color: #2C3E50; margin-top: 15px;">
        Plataforma de Noticias
    </div>
    """,
    unsafe_allow_html=True,
)

# Menú de navegación en la barra lateral
with st.sidebar:
    menu = option_menu(
        menu_title="Menú Principal",  # Título del menú
        options=["Noticias Relevantes", "Selector de Noticias", "Gráficos Interactivos", "Miembros del Proyecto"],  # Opciones
        icons=["newspaper", "filter", "bar-chart", "people"],  # Íconos de cada opción
        menu_icon="cast",  # Ícono principal del menú
        default_index=0,  # Primera opción seleccionada por defecto
        orientation="vertical",
    )

# Mostrar contenido dinámico según la sección seleccionada
if menu == "Noticias Relevantes":
    st.subheader("Noticias Relevantes")
    st.write("Aquí puedes ver las noticias más destacadas.")
elif menu == "Selector de Noticias":
    st.subheader("Selector de Noticias")
    st.write("Filtra y selecciona las noticias que te interesen.")
elif menu == "Gráficos Interactivos":
    st.subheader("Gráficos Interactivos")
    st.write("Explora los gráficos generados a partir de las noticias.")
elif menu == "Miembros del Proyecto":
    st.subheader("Miembros del Proyecto")
    st.write("""
    - **Miembro 1**: Analista de datos  
    - **Miembro 2**: Especialista en visualización  
    - **Miembro 3**: Ingeniero en IA  
    - **Miembro 4**: Desarrollador web  
    """)
