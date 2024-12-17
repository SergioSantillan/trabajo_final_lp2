import streamlit as st

# Título de la aplicación
st.title("Mi Primera Plataforma en Streamlit")

# Descripción inicial
st.write("¡Bienvenido/a! Aquí puedes explorar datos, gráficos y más.")

# Carga de datos (si tienes un archivo CSV)
uploaded_file = st.file_uploader("Sube un archivo CSV", type="csv")

if uploaded_file:
    import pandas as pd
    data = pd.read_csv(uploaded_file)
    st.write("Vista previa de los datos:")
    st.dataframe(data.head())

# Gráficos interactivos
st.write("Gráfico interactivo")
if uploaded_file:
    st.line_chart(data)

# Footer
st.sidebar.title("Navegación")
st.sidebar.write("Añade más opciones aquí.")
