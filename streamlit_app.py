import streamlit as st

# Configuración básica
st.set_page_config(page_title="Mi Plataforma", layout="wide")

# Título principal
st.title("Plataforma de Noticias y Visualización")
st.markdown("Esta plataforma te permite explorar noticias relevantes, gráficos interactivos y más.")

# Navegación con botones en la barra lateral
st.sidebar.title("Navegación")
opcion = st.sidebar.radio(
    "Elige una sección:",
    ["Noticias Relevantes", "Selector de Noticias", "Gráficos Interactivos", "Miembros del Proyecto"]
)

# Noticias Relevantes
if opcion == "Noticias Relevantes":
    st.subheader("Noticias Relevantes")
    st.write("Aquí puedes ver las noticias más destacadas.")
    # Ejemplo: Mostrar una tabla de noticias relevantes
    st.write("Pronto se mostrarán las noticias más relevantes aquí.")

# Selector de Noticias
elif opcion == "Selector de Noticias":
    st.subheader("Selector de Noticias")
    st.write("Filtra y selecciona las noticias que te interesen.")
    # Ejemplo: Un filtro por palabras clave
    palabra_clave = st.text_input("Busca por palabra clave:")
    if palabra_clave:
        st.write(f"Resultados para: **{palabra_clave}**")
        # Agrega lógica para filtrar noticias según la palabra clave

# Gráficos Interactivos
elif opcion == "Gráficos Interactivos":
    st.subheader("Gráficos Interactivos")
    st.write("Explora los gráficos generados a partir de las noticias.")
    # Ejemplo: Mostrar un gráfico de prueba
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Datos de ejemplo
    data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
    st.line_chart(data)

# Miembros del Proyecto
elif opcion == "Miembros del Proyecto":
    st.subheader("Miembros del Proyecto")
    st.write("Conoce a los integrantes del equipo.")
    # Ejemplo: Mostrar una lista de miembros
    st.write("""
    - **Miembro 1**: Analista de datos  
    - **Miembro 2**: Especialista en visualización  
    - **Miembro 3**: Ingeniero en IA  
    - **Miembro 4**: Desarrollador web  
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Gracias por usar nuestra plataforma.")

