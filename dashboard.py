import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import openpyxl

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
)

st.title("# Bienvenue sur l'outil de monitoring! 👋")

st.sidebar.success("Selectionner la technologie à monitorer.")

st.markdown(
    """
    \n\n\n
    Cet outil a été développé dans un premier temps pour monitorer certaines métriques 
    des technologies 3G et 4G mais aussi pour pouvoir générer un ranking des worst cells.
    \n
    **👈 Veuillez selectionner une technologie** à monitorer !
    \n\n
"""
)

image="pexels-eberhard-grossgasteiger-2098404.jpg"
st.image(image)





