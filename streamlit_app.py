import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud 
# Configuración de la página
st.set_page_config(page_title="Análisis de Noticias", layout="wide")

# Título y descripción principal
st.title("Análisis de Noticias Interactivas")
st.write("Explora las noticias a través de gráficos interactivos y análisis avanzados.")

# Función para cargar datos
@st.cache_data
def load_data(file_path=None):
    if file_path:
        return pd.read_csv(file_path)
    else:
        # Datos de ejemplo
        return pd.DataFrame({
            'category': ['Política', 'Deportes', 'Cultura', 'Tecnología', 'Economía', 
                         'Deportes', 'Cultura', 'Política', 'Tecnología', 'Política'],
            'title': ['Noticia 1', 'Noticia 2', 'Noticia 3', 'Noticia 4', 'Noticia 5', 
                      'Noticia 6', 'Noticia 7', 'Noticia 8', 'Noticia 9', 'Noticia 10']
        })

# Carga de datos desde la barra lateral
st.sidebar.header("Opciones de datos")
data_source = st.sidebar.radio("Selecciona la fuente de datos:", ("Cargar desde archivo", "Usar datos de ejemplo"))

if data_source == "Cargar desde archivo":
    uploaded_file = st.sidebar.file_uploader("Carga tu archivo CSV", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        st.warning("Por favor, carga un archivo para continuar.")
        st.stop()
else:
    df = load_data()

# Mostrar los datos cargados
st.subheader("Datos Cargados")
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df)

# Análisis y Gráficos Interactivos
st.subheader("Gráficos Interactivos")

if not df.empty:
    # Gráfico 1: Top 5 Categorías
    st.markdown("### Gráfico 1: Top 5 Categorías con Más Noticias")
    top_categories = df['category'].value_counts().head(5).reset_index()
    top_categories.columns = ['Categoría', 'Cantidad']

    fig1 = px.bar(
        top_categories, x='Categoría', y='Cantidad', 
        title='Top 5 Categorías con más Noticias', color='Categoría'
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 2: Distribución de Noticias
    st.markdown("### Gráfico 2: Distribución de Noticias por Categoría")
    fig2 = px.pie(
        df, names='category', 
        title='Distribución de Noticias por Categoría', hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfico 3: Número de Noticias por Categoría
    st.markdown("### Gráfico 3: Evolución del Número de Noticias")
    df['count'] = 1  # Contador ficticio para la suma
    time_series = df.groupby('category')['count'].sum().reset_index()
    fig3 = px.line(
        time_series, x='category', y='count', 
        title='Tendencia de Noticias por Categoría', markers=True
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Gráfico 4: Gráfico de Dispersión de Categorías
    st.markdown("### Gráfico 4: Dispersión de Categorías")
    fig4 = px.scatter(
        df, x='category', y='title', 
        title='Relación entre Categorías y Noticias', color='category'
    )
    st.plotly_chart(fig4, use_container_width=True)

    # Gráfico 5: Nube de Palabras
    st.markdown("### Gráfico 5: Nube de Palabras de los Títulos de Noticias")

    # Configurar paleta de colores
    color_palette = ["#FFF700", "#FF1717", "#2917ED", "#25a146"]

    def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return random.choice(color_palette)

    # Crear nube de palabras
    titles = df['title'].dropna().tolist()
    text = " ".join(titles)
    wordcloud = WordCloud(
        width=800, height=400, background_color='white', 
        max_words=100, color_func=random_color_func, 
        contour_color='black', contour_width=1
    ).generate(text)

    # Mostrar nube de palabras
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title("Nube de Palabras de los Títulos de Noticias", fontsize=18, fontweight='bold')
    st.pyplot(fig)
else:
    st.error("El conjunto de datos está vacío. Verifica el archivo cargado.")
