# 🚇 PredicTrafic | IA & Mobilité

Projet de fin de module Yboost Data & IA réalisé dans le cadre du cursus Data Analyst à **Paris YNOV Campus**.

## 📝 Description
**PredicTrafic** est une solution d'aide à la décision intelligente pour la gestion des flux de transport en Île-de-France. Grâce à une approche basée sur le Machine Learning, l'application permet de prédire l'affluence des passagers en fonction de variables temporelles et météorologiques, offrant aux opérateurs une vision claire et dynamique du réseau.

## 🚀 Fonctionnalités Principales

* **🌍 Radar Global (Live) :** Visualisation 3D en temps réel des flux de passagers sur les 25 hubs principaux.
* **💥 simulateur de Crise :** Fonctionnalité "Chaos Engineering" pour injecter des incidents (fermetures de gares) et visualiser l'impact sur le réseau.
* **🛤️ Smart Routing :** Calculateur d'itinéraire utilisant la formule de Haversine avec ajustement dynamique des temps de trajet selon l'affluence.
* **🔍 Audit IA :** Analyse de la performance du modèle (Random Forest) et visualisation de l'importance des variables prédictives.

## 🛠️ Stack Technique

* **Langage :** Python
* **Dashboard :** Streamlit
* **Machine Learning :** Scikit-Learn (Random Forest)
* **Cartographie :** PyDeck (données OpenStreetMap/CARTO)
* **Manipulation Data :** Pandas, NumPy

## ⚙️ Installation & Lancement

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/Amine06-ch/PREDICTRAFIC-IA-MOBILIT-.git](https://github.com/Amine06-ch/PREDICTRAFIC-IA-MOBILIT-.git)
   cd PREDICTRAFIC-IA-MOBILIT-
Installer les dépendances :

Bash
pip install -r requirements.txt
Lancer l'application :

Bash
streamlit run app.py
📂 Structure du projet
Plaintext
├── data/               # Dataset source (csv)
├── models/             # Modèles IA entraînés (.pkl)
├── scripts/            # Scripts de construction de données et d'entraînement
├── app.py              # Application Streamlit principale
└── requirements.txt    # Dépendances du projet



👤 Auteur
Amine Chachou - Étudiant en Data & IA - Paris YNOV Campus


---


