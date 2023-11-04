import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.dataframe_explorer import dataframe_explorer
import time
from datetime import datetime
import openpyxl
import altair as alt
from urllib.error import URLError

import dashboard

st.set_page_config(page_title="Monitoring WCDMA", page_icon="📈")

st.markdown("# Monitoring WCDMA")
st.sidebar.header("Monitoring WCDMA")
st.write(
    """Ici nous allons monitorer les KPIs WCDMA les plus significatifs."""
)

#st.header(":grey[Upload du fichier d'input] 📑", divider='grey')

uploaded_file = st.file_uploader("Choisir un fichier")
if uploaded_file is not None:
    df_data_wcdma = pd.read_excel(uploaded_file, sheet_name='Data', skiprows=[0])
    df_data_wcdma.dropna(subset=['PLMN Name'], inplace=True)
    df_doc_wcdma = pd.read_excel(uploaded_file, sheet_name='Documentation', 
                               skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    
    with st.expander("Visualiser les tables uploadées"):
        st.dataframe(df_data_wcdma)
        st.dataframe(df_doc_wcdma)

    # Créer une liste des KPIs taux (Unit == "[%]")
    kpi_taux = df_doc_wcdma[df_doc_wcdma["Unit"] == "[%]"]["KPI Alias"].tolist()

    # Créer une liste des KPIs numériques (Unit == "[#]")
    kpi_num = df_doc_wcdma[df_doc_wcdma["Unit"] == "[#]"]["KPI Alias"].tolist()

    # Liste pour stocker les graphiques
    #fig_list = []

    try:

        # Sélection des KPIs
        selected_kpis = st.multiselect("Sélectionnez les KPIs à surveiller", df_doc_wcdma["KPI Alias"].unique())

        # Obtenir les valeurs uniques de la colonne "PLMN Name" de df_data_wcdma
        plmn_values = df_data_wcdma["PLMN Name"].unique()

        # Sélection des éléments (PLMN Name) à surveiller en fonction des valeurs uniques
        selected_elements = st.multiselect("Sélectionnez les éléments à surveiller (PLMN Name)", plmn_values)

        if not (selected_kpis or selected_elements):
            st.error("Veuillez selectionner au moins un élément et au moins un KPI svp.")
        else:
            # Filtrer df_data_wcdma en fonction des sélections
            filtered_data = df_data_wcdma[df_data_wcdma["PLMN Name"].isin(selected_elements)]

            # Créer un graphique interactif pour tous les KPI sélectionnés
            if selected_kpis:
                # Visualisation interactive pour les KPI
                fig = go.Figure()
                fig.update_layout(
                    title="Visualisation interactive pour les KPI sélectionnés",
                    xaxis_title="Période"
                )

                for kpi in selected_kpis:
                    kpi_data = filtered_data
                    if kpi in kpi_taux:
                        # Ajouter une trace de ligne pour le KPI taux
                        fig.add_trace(go.Line(x=kpi_data["Period start time"], 
                                                 y=kpi_data[kpi], name=kpi, yaxis="y1"))
                    elif kpi in kpi_num:
                        # Ajouter une trace d'histogramme pour le KPI nombre
                        fig.add_trace(go.Bar(x=kpi_data["Period start time"], 
                                                   y=kpi_data[kpi], name=kpi, opacity=0.5, yaxis="y2"))

                # Personnalisation de l'axe Y pour les KPI de type taux (à gauche)
                fig.update_layout(yaxis_title="KPI(s) [ % ]")

                # Personnalisation de l'axe Y2 pour les KPI de type nombre (à droite)
                fig.update_layout(yaxis2=dict(overlaying='y1', side='right'), yaxis2_title="KPI(s) [ # ]")

                # Personnalisation des axes et du titre
                fig.update_layout(
                    xaxis_title="Période",
                    title="Visualisation interactive pour les KPI sélectionnés"
                )

                # Afficher le graphique interactif
                st.write(fig)


    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
            """
            % e.reason
        )




    
  
