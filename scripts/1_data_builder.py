import pandas as pd
import numpy as np
import os

print("🔄 Initialisation du Pipeline Data Engineering...")
np.random.seed(42)
n_lignes = 50000 # On passe à 50 000 lignes pour un vrai volume Data

# Les 25 hubs stratégiques du réseau francilien avec leurs pondérations
hubs = {
    'Châtelet-Les Halles': 1.6, 'Gare du Nord': 1.5, 'La Défense': 1.4,
    'Gare de Lyon': 1.3, 'Montparnasse': 1.1, 'Saint-Lazare': 1.2,
    'Auber / Opéra': 1.1, 'Nation': 1.0, 'République': 0.9,
    'Bercy': 0.8, 'Val de Fontenay': 0.85, 'Neuilly-Plaisance': 0.6,
    'Noisy-le-Grand': 0.75, 'Marne-la-Vallée (Chessy)': 0.9, 'Vincennes': 0.7,
    'Cergy-Préfecture': 0.8, 'Massy-Palaiseau': 0.85, 'Juvisy': 0.75,
    'Aéroport CDG 2': 1.1, 'Aéroport d\'Orly': 0.9, 'Versailles-Chantiers': 0.8,
    'Saint-Denis (Stade)': 0.85, 'Créteil-Préfecture': 0.7,
    'Boulogne - Pont de Sèvres': 0.65, 'Nanterre-Préfecture': 0.75
}

stations = np.random.choice(list(hubs.keys()), n_lignes)
heures = np.random.randint(5, 24, n_lignes)
jours = np.random.choice(['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'], n_lignes)
meteo = np.random.choice(['Soleil', 'Pluie', 'Nuageux'], n_lignes)

# Logique de simulation métier
base_flux = heures * 15
base_flux = np.where((heures >= 7) & (heures <= 9), base_flux * 3.0, base_flux)   # Pic matin
base_flux = np.where((heures >= 17) & (heures <= 19), base_flux * 3.5, base_flux) # Pic soir
base_flux = np.where(meteo == 'Pluie', base_flux * 1.2, base_flux)                # Report lié à la pluie
base_flux = np.where(np.isin(jours, ['Samedi', 'Dimanche']), base_flux * 0.6, base_flux) # Chute le weekend

# Application du poids spécifique de chaque gare
poids_array = np.array([hubs[s] for s in stations])
affluence = np.abs((base_flux * poids_array) + np.random.normal(0, 50, n_lignes)).astype(int)

df = pd.DataFrame({'Station': stations, 'Heure': heures, 'Jour': jours, 'Meteo': meteo, 'Affluence': affluence})

os.makedirs('data', exist_ok=True)
df.to_csv('data/dataset_complet.csv', index=False)
print("✅ Base de données générée : data/dataset_complet.csv (50 000 enregistrements)")