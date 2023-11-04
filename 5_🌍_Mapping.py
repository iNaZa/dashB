import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
#import pydeck as pdk
#import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="MAP Free Caraïbes", page_icon="🌎")

st.markdown("# Map Free Caraïbes")
st.sidebar.header("Map Free Caraïbes")
st.write(
    """Cartographie des boutiques et bornes présentent dans la région des Caraïbes"""
)

#df_boutiques = pd.read_csv("adresses_boutiques_bornes_free_caraibes.csv", sep=";", encoding='ISO-8859-1')
df_boutiques_v2 = pd.read_csv("adresses_boutiques_bornes_free_caraibes_v2.csv", sep=";", encoding='ISO-8859-1')


# Créer un géocodeur
geolocator = Nominatim(user_agent="geoapiExercises")


#Afficher Map
st.map(df_boutiques_v2.dropna(subset=['latitude', 'longitude']), size=100, color='#ff1100', )

# Afficher le DataFrame mis à jour

with st.expander("Visualiser les détails des boutiques et bornes de Free Caraïbes. 👇"):
        st.dataframe(df_boutiques_v2)



# Fonction pour obtenir la latitude et la longitude à partir de l'adresse
#@st.cache_data
#def get_lat_lon(address):
#    location = geolocator.geocode(address)
#    if location:
#        return location.latitude, location.longitude
#    else:
#        return None, None

# Appliquer la fonction pour obtenir les coordonnées
#df_boutiques['latitude'], df_boutiques['longitude'] = zip(*df_boutiques['Adresse'].apply(get_lat_lon))



