import streamlit as st

# Configuración básica
st.set_page_config(page_title="Plataforma", layout="wide")

# Título principal
st.title("Plataforma de Noticias")
st.markdown("Usa los botones para navegar entre las secciones:")

# Crear botones estilizados usando HTML y CSS
button_styles = """
<style>
    .btn {
        display: inline-block;
        background-color: #007BFF; /* Color de fondo */
        color: white;             /* Color del texto */
        padding: 10px 20px;       /* Espaciado interno */
        font-size: 16px;          /* Tamaño de letra */
        border: none;             /* Sin bordes por defecto */
        border-radius: 25px;      /* Bordes redondeados */
        text-align: center;       /* Centrar texto */
        text-decoration: none;    /* Sin subrayado */
        margin: 10px 5px;         /* Espaciado entre botones */
        cursor: pointer;          /* Cambiar cursor al pasar */
        transition: 0.3s;         /* Animación suave */
    }
    .btn:hover {
        background-color: #0056b3; /* Cambiar color al pasar el ratón */
    }
</style>
"""

st.markdown(button_styles, unsafe_allow_html=True)

# HTML para los botones
botones = """
<div style="text-align: center;">
    <a href="?section=Noticias Relevantes" class="btn">Noticias Relevantes</a>
    <a href="?section=Selector de Noticias" class="btn">Selector de Noticias</a>
    <a href="?section=Gráficos Interactivos" class="btn">Gráficos Interactivos</a>
    <a href="?section=Miembros del Proyecto" class="btn">Miembros del Proyecto</a>
</div>
"""

st.markdown(botones, unsafe_allow_html=True)

# Obtener la sección seleccionada desde la URL
seccion = st.experimental_get_query_params().get("section", [""])[0]

# Mostrar contenido según la sección seleccionada
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

# Mensaje por defecto
else:
    st.write("Selecciona una sección para explorar más.")
