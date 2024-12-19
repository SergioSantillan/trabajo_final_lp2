import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración básica de la app
st.set_page_config(page_title="Análisis de Noticias", layout="wide")

# Título y descripción
st.title("Análisis de Noticias por Categorías")
st.write("""
Esta aplicación permite analizar noticias agrupadas por categorías, visualizando las categorías más frecuentes y otros detalles interesantes.
""")

# Carga de datos
@st.cache_data
def load_data(file_path=None):
    if file_path:
        return pd.read_csv(file_path)  # Reemplaza con la ruta de tu archivo CSV
    else:
        # Datos de ejemplo
        return pd.DataFrame({
            'category': ['Política', 'Deportes', 'Cultura', 'Tecnología', 'Economía', 
                         'Deportes', 'Cultura', 'Política', 'Tecnología', 'Política'],
            'title': ['Noticia 1', 'Noticia 2', 'Noticia 3', 'Noticia 4', 'Noticia 5', 
                      'Noticia 6', 'Noticia 7', 'Noticia 8', 'Noticia 9', 'Noticia 10']
        })

# Sidebar: Subir archivo o usar datos predeterminados
st.sidebar.header("Opciones de datos")
data_source = st.sidebar.radio(
    "Selecciona la fuente de datos:",
    ("Cargar desde archivo", "Usar datos de ejemplo")
)

if data_source == "Cargar desde archivo":
    uploaded_file = st.sidebar.file_uploader("Carga tu archivo CSV", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        st.warning("Por favor, carga un archivo para continuar.")
        st.stop()
else:
    df = load_data()

# Mostrar el DataFrame en la página principal
st.subheader("Datos Cargados")
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df)

# Análisis de datos
if df.empty:
    st.error("El conjunto de datos está vacío. Verifica el archivo cargado.")
else:
    try:
        # **Gráfico 1: Top 5 Categorías**
        st.subheader("Gráfico: Top 5 Categorías con Más Noticias")
        top_categories = df['category'].value_counts().head(5).reset_index()
        top_categories.columns = ['Categoría', 'Cantidad']

        fig1 = px.bar(
            data_frame=top_categories,
            x='Categoría',
            y='Cantidad',
            title='Top 5 Categorías con más Noticias',
            labels={'Categoría': 'Categoría', 'Cantidad': 'Cantidad'},
            color='Categoría'
        )

        st.plotly_chart(fig1, use_container_width=True)

        # **Gráfico 2: Distribución de Noticias por Categoría**
        st.subheader("Gráfico: Distribución de Noticias por Categoría")
        fig2 = px.pie(
            data_frame=df,
            names='category',
            title='Distribución de Noticias por Categoría',
            hole=0.4,
            labels={'category': 'Categoría'}
        )

        st.plotly_chart(fig2, use_container_width=True)

    except Exception as e:
        st.error(f"Se produjo un error durante el análisis: {e}")

# Información adicional
st.sidebar.info("""
Crea gráficos interactivos con tus propios datos y explora las categorías principales.
""")

