import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
import math


st.set_page_config(page_title="PredicTrafic IA - Command Center", layout="wide", page_icon="🚇")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    h1 { color: #d4af37 !important; text-align: center; font-size: 45px !important; font-weight: 900; letter-spacing: 2px;}
    h2, h3 { color: #d4af37 !important; font-weight: 400; }
    .stMetric { background-color: #0a0a0a !important; border: 1px solid #333 !important; border-top: 3px solid #d4af37 !important; border-radius: 5px; padding: 15px;}
    div[data-testid="stSidebar"] { background-color: #000000; border-right: 1px solid #222; }
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_assets():
    model = joblib.load('models/rf_model.pkl')
    features = joblib.load('models/features.pkl')
    return model, features

model, features = load_assets()

hubs = {
    'Châtelet-Les Halles': {'lat': 48.8619, 'lon': 2.3470, 'poids': 1.6},
    'Gare du Nord': {'lat': 48.8809, 'lon': 2.3553, 'poids': 1.5},
    'La Défense': {'lat': 48.8919, 'lon': 2.2386, 'poids': 1.4},
    'Gare de Lyon': {'lat': 48.8443, 'lon': 2.3744, 'poids': 1.3},
    'Montparnasse': {'lat': 48.8410, 'lon': 2.3204, 'poids': 1.1},
    'Saint-Lazare': {'lat': 48.8763, 'lon': 2.3253, 'poids': 1.2},
    'Auber / Opéra': {'lat': 48.8726, 'lon': 2.3284, 'poids': 1.1},
    'Nation': {'lat': 48.8482, 'lon': 2.3959, 'poids': 1.0},
    'République': {'lat': 48.8675, 'lon': 2.3638, 'poids': 0.9},
    'Bercy': {'lat': 48.8396, 'lon': 2.3800, 'poids': 0.8},
    'Val de Fontenay': {'lat': 48.8550, 'lon': 2.4900, 'poids': 0.85},
    'Neuilly-Plaisance': {'lat': 48.8527, 'lon': 2.4936, 'poids': 0.6},
    'Noisy-le-Grand': {'lat': 48.8395, 'lon': 2.5495, 'poids': 0.75},
    'Marne-la-Vallée (Chessy)': {'lat': 48.8698, 'lon': 2.7836, 'poids': 0.9},
    'Vincennes': {'lat': 48.8475, 'lon': 2.4402, 'poids': 0.7},
    'Cergy-Préfecture': {'lat': 49.0359, 'lon': 2.0805, 'poids': 0.8},
    'Massy-Palaiseau': {'lat': 48.7251, 'lon': 2.2592, 'poids': 0.85},
    'Juvisy': {'lat': 48.6865, 'lon': 2.3776, 'poids': 0.75},
    'Aéroport CDG 2': {'lat': 49.0097, 'lon': 2.5479, 'poids': 1.1},
    'Aéroport d\'Orly': {'lat': 48.7293, 'lon': 2.3632, 'poids': 0.9},
    'Versailles-Chantiers': {'lat': 48.7957, 'lon': 2.1352, 'poids': 0.8},
    'Saint-Denis (Stade)': {'lat': 48.9244, 'lon': 2.3556, 'poids': 0.85},
    'Créteil-Préfecture': {'lat': 48.7801, 'lon': 2.4542, 'poids': 0.7},
    'Boulogne - Pont de Sèvres': {'lat': 48.8298, 'lon': 2.2285, 'poids': 0.65},
    'Nanterre-Préfecture': {'lat': 48.8966, 'lon': 2.2155, 'poids': 0.75}
}


st.sidebar.markdown("## ⚙️ SYSTÈME IA")
page = st.sidebar.radio("Modules du Système", ["🌍 Radar Global (Live)", "🛤️ Redirection IA (Routing)"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎛️ Paramètres Environnement")
h_in = st.sidebar.slider("Horloge Système (H)", 5, 23, 18)
j_in = st.sidebar.selectbox("Jour Actuel", ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'])
m_in = st.sidebar.selectbox("Météo Observée", ['Soleil', 'Pluie', 'Nuageux'])

st.title("🚇 PREDICTRAFIC | IA & MOBILITÉ")
st.markdown("---")


input_df = pd.DataFrame([{'Heure': h_in, 'Jour': j_in, 'Meteo': m_in}])
input_encoded = pd.get_dummies(input_df).reindex(columns=features, fill_value=0)
base_prediction = int(model.predict(input_encoded)[0])


if page == "🌍 Radar Global (Live)":
    
    incident_mode = st.toggle("💥 Injecter Incident (Fermeture Châtelet & Gare du Nord)", value=False)
    
    
    seuil_critique = 1600 * 125 
    flux_total = base_prediction * 125 
    
    if incident_mode:
        flux_total = int(flux_total * 1.45)
    
    taux_saturation_reel = (flux_total / seuil_critique) * 100
    taux_affiche = min(taux_saturation_reel, 100)

    c1, c2, c3 = st.columns(3)
    c1.metric("Volume Réseau Instantané", f"{flux_total:,} passagers")
    
    if taux_affiche == 100:
        c2.metric("Taux de Saturation IA", "100.0% MAX")
    else:
        c2.metric("Taux de Saturation IA", f"{taux_affiche:.1f}%")
        
    if incident_mode:
        c3.metric("Statut", "🔴 INCIDENT MAJEUR", "Effondrement du réseau")
    elif taux_affiche > 85:
        c3.metric("Statut", "⚠️ SURCHARGE", "Rames supplémentaires requises")
    else:
        c3.metric("Statut", "🟢 FLUIDE", "Trafic Nominal")

    
    stations_list = []
    for nom, data in hubs.items():
        flux = int(data['poids'] * base_prediction)
        if incident_mode:
            if nom in ['Châtelet-Les Halles', 'Gare du Nord']: 
                flux = 0
            else: 
                flux = int(flux * 1.45) 
        
        couleur = [30,30,30,150] if flux == 0 else ([220,20,60,255] if flux > 2000 else [212,175,55,200])
        stations_list.append({'Station': nom, 'lat': data['lat'], 'lon': data['lon'], 'Flux': flux, 'Couleur': couleur})
        
    df_map = pd.DataFrame(stations_list)

    view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=9.5, pitch=55, bearing=0)
    layer_col = pdk.Layer(
        "ColumnLayer", data=df_map, get_position="[lon, lat]", get_elevation="Flux",
        elevation_scale=2.5, radius=350, get_fill_color="Couleur", pickable=True, auto_highlight=True,
    )
    st.pydeck_chart(pdk.Deck(map_style=None, layers=[layer_col], initial_view_state=view_state, 
                             tooltip={"text": "🚉 {Station}\nFlux prédictif: {Flux} passagers"}))


elif page == "🛤️ Redirection IA (Routing)":
    st.markdown("### 🛤️ Calculateur d'Itinéraire Prédictif (Haversine)")
    st.write("Analyse géospatiale de la distance et calcul dynamique des retards induits par l'affluence.")

    col1, col2 = st.columns(2)
    with col1:
        depart = st.selectbox("Gare de Départ", list(hubs.keys()), index=0)
    with col2:
        arrivee = st.selectbox("Gare d'Arrivée", list(hubs.keys()), index=13)

    if depart == arrivee:
        st.warning("Veuillez sélectionner deux gares différentes.")
    else:
       
        lat1, lon1 = hubs[depart]['lat'], hubs[depart]['lon']
        lat2, lon2 = hubs[arrivee]['lat'], hubs[arrivee]['lon']
        
        R = 6371 
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance_km = R * c
        
       
        temps_theorique = int((distance_km / 40) * 60) + 5
        
        flux_depart = int(hubs[depart]['poids'] * base_prediction)
        flux_arrivee = int(hubs[arrivee]['poids'] * base_prediction)
        
        retard_depart = max(0, (flux_depart - 1500) // 150) 
        retard_arrivee = max(0, (flux_arrivee - 1500) // 150)
        temps_total = temps_theorique + retard_depart + retard_arrivee

        c_res1, c_res2, c_res3, c_res4 = st.columns(4)
        c_res1.metric("Distance Géodesique", f"{distance_km:.1f} km")
        c_res2.metric("Temps de parcours estimé", f"{temps_total} min", f"+{retard_depart+retard_arrivee} min d'affluence", delta_color="inverse")
        c_res3.metric(f"Charge {depart}", f"{flux_depart} pax")
        c_res4.metric(f"Charge {arrivee}", f"{flux_arrivee} pax")

     
        arc_data = pd.DataFrame([{
            "source_lon": hubs[depart]['lon'], "source_lat": hubs[depart]['lat'],
            "target_lon": hubs[arrivee]['lon'], "target_lat": hubs[arrivee]['lat']
        }])

        view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=9.5, pitch=45)
        
        arc_layer = pdk.Layer(
            "ArcLayer", data=arc_data,
            get_source_position=["source_lon", "source_lat"], get_target_position=["target_lon", "target_lat"],
            get_source_color=[212, 175, 55, 255], get_target_color=[220, 20, 60, 255], get_width=6
        )
        
        df_fond = pd.DataFrame([{'lat': v['lat'], 'lon': v['lon'], 'Flux': 300} for k, v in hubs.items()])
        col_layer = pdk.Layer("ColumnLayer", data=df_fond, get_position="[lon, lat]", get_elevation="Flux", radius=150, get_fill_color=[50,50,50,150])

        st.pydeck_chart(pdk.Deck(map_style=None, layers=[col_layer, arc_layer], initial_view_state=view_state))