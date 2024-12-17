import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Plataforma de Noticias", layout="wide")

# Título principal
st.title("Plataforma de Noticias")
st.markdown("Usa los botones en la barra lateral para navegar entre las secciones.")

# Estilo CSS para los botones de la barra lateral
button_styles = """
<style>
    .sidebar .stButton > button {
        background-color: #007BFF; /* Color de fondo */
        color: white;             /* Color del texto */
        padding: 10px 20px;       /* Espaciado interno */
        font-size: 16px;          /* Tamaño de letra */
        border: none;             /* Sin bordes */
        border-radius: 25px;      /* Bordes redondeados */
        text-align: center;       /* Centrar texto */
        cursor: pointer;          /* Cambiar cursor al pasar */
        transition: 0.3s;         /* Animación suave */
    }
    .sidebar .stButton > button:hover {
        background-color: #0056b3; /* Cambiar color al pasar el ratón */
    }
</style>
"""

st.markdown(button_styles, unsafe_allow_html=True)

# Barra lateral con botones
with st.sidebar:
    st.header("Navegación")
    if st.button("Noticias Relevantes"):
        st.session_state.seccion = "Noticias Relevantes"
    if st.button("Selector de Noticias"):
        st.session_state.seccion = "Selector de Noticias"
    if st.button("Gráficos Interactivos"):
        st.session_state.seccion = "Gráficos Interactivos"
    if st.button("Miembros del Proyecto"):
        st.session_state.seccion = "Miembros del Proyecto"

# Mostrar contenido según la sección seleccionada
seccion = st.session_state.get("seccion", "Noticias Relevantes")

if seccion == "Noticias Relevantes":
    st.subheader("Noticias Relevantes")
    st.write("Aquí puedes ver las noticias más destacadas.")
elif seccion == "Selector de Noticias":
    st.subheader("Selector de Noticias")
    st.write("Filtra y selecciona las noticias que te interesen.")
elif seccion == "Gráficos Interactivos":
    st.subheader("Gráficos Interactivos")
    st.write("Explora los gráficos generados a partir de las noticias.")
elif seccion == "Miembros del Proyecto":
    st.subheader("Miembros del Proyecto")
    st.write("""
    - **Miembro 1**: Analista de datos  
    - **Miembro 2**: Especialista en visualización  
    - **Miembro 3**: Ingeniero en IA  
    - **Miembro 4**: Desarrollador web  
    """)
