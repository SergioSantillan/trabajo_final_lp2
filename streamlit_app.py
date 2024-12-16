import streamlit as st
import pandas as pd
from wordcloud import WordCloud

st.set_page_config(
  page_title="Home",
  page_icon="🏠️"
)

def generate_cloud(text):
  """Generate a word cloud"""
  wc = WordCloud(
    width=600,
    height=600,
    max_words=2000,
    margin=0
  ).generate(text)

  return wc

st.write("# Fake News Classifier")

st.image(
  "./roman-kraft-_Zua2hyvTBk-unsplash.jpg"
)

st.markdown(
  """
  ## Introduction
  A type of yellow journalism, fake news encapsulates pieces of news
  that may be hoaxes and is generally spread through social media and
  other online media.
  This is often done to further or impose certain ideas 
  and is often achieved with political agendas.
  Such news items may contain false and/or exaggerated claims,
  and may end up being viralized by algorithms,
  and users may end up in a filter bubble.

  ## Objective
  The aim of this project is to build a model to accurately
   **classify** a piece of news as **REAL** or **FAKE**.

  ## Data Description
  This dataset has a shape of 7796 × 4. 
  The first column identifies the news, 
  the second and third are the title and text, 
  and the fourth column has labels denoting whether the news is REAL or FAKE.
  """
)

df = pd.read_csv("./Model/news.csv")
df.drop('Unnamed: 0', inplace=True, axis=1)
if (st.checkbox("Show Data")):
  x = st.slider("Rows", 5, 20, 10)
  st.dataframe(df.head(x))

st.markdown(
  """
  - `title`:    Represents the title of the news article.
  - `text`:     The text containing the news in details
  - `label`:    Classification into **REAL** or **FAKE**
  """
)
