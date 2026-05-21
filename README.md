# 🚇 PredicTrafic IA — Control Center V5

## 📌 Présentation

**PredicTrafic IA** est une plateforme intelligente de supervision et de prédiction des flux de transports franciliens.

Le projet combine :

* 🤖 Intelligence artificielle prédictive
* 🌦️ météo temps réel
* 🚆 Open Data transport (Île-de-France Mobilités)
* 🗺️ visualisation 3D interactive
* 🔥 simulation de crise
* 🧭 routing intelligent
* 📊 dashboard opérateur temps réel

L’objectif est de proposer une base crédible de système d’aide à la décision pour les opérateurs de mobilité urbaine.

---

# ✨ Fonctionnalités principales

## 📊 Dashboard Live

* supervision réseau en temps réel
* indicateurs de saturation
* contrôle centralisé
* état du trafic simulé
* assistant IA

## 🗺️ Cartographie 3D

* hubs stratégiques franciliens
* colonnes dynamiques selon l’affluence
* visualisation PyDeck / Deck.GL

## 🌦️ Météo réelle OpenWeather

* récupération météo live
* impact météo sur les flux
* scénarios dynamiques

## 🚆 API Île-de-France Mobilités

* connexion API IDFM
* supervision des perturbations
* architecture compatible open data temps réel

## 🧭 Routing IA

* estimation du temps de trajet
* risque de saturation
* alternatives intelligentes

## 🔥 Simulateur de crise

* fermeture de stations
* redistribution des flux
* gestion d’incident

## 🧠 Audit IA

* analyse des performances du modèle
* importance des variables
* heatmaps horaires
* analyse météo

## 📁 Export CSV

* export des états réseau
* export des simulations
* export des prévisions

---

# 🧩 Stack Technique

| Domaine       | Technologie        |
| ------------- | ------------------ |
| Frontend      | Streamlit          |
| IA / ML       | Random Forest      |
| Data          | Pandas / NumPy     |
| Cartographie  | PyDeck / Deck.GL   |
| APIs          | OpenWeather / IDFM |
| Visualisation | Streamlit UI       |
| Export        | CSV                |

---

# 🚀 Installation

## 1. Cloner le projet

```bash
git clone https://github.com/Amine06-ch/PREDICTRAFIC-IA-MOBILIT-.git
cd PREDICTRAFIC-IA-MOBILIT-
```

---

## 2. Créer l’environnement virtuel

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou :

```bash
pip install streamlit pandas numpy==1.26.4 pydeck joblib scikit-learn requests python-dotenv altair==5.3.0
```

---

## 4. Lancer le projet

```bash
streamlit run app.py
```

---

# 🔑 Configuration API

Créer un fichier `.env` :

```env
OPENWEATHER_API_KEY=VOTRE_CLE
IDFM_API_KEY=VOTRE_CLE
```

---

# 📈 État actuel du projet

| Version                  | Statut |
| ------------------------ | ------ |
| V1 — Prototype ML        | ✅      |
| V2 — Dashboard opérateur | ✅      |
| V3 — Simulation de crise | ✅      |
| V4 — Météo temps réel    | ✅      |
| V5 — Connexion API IDFM  | ✅      |

---

# 🛣️ Roadmap future

* notifications voyageurs temps réel
* exploitation détaillée des perturbations IDFM
* déploiement cloud
* comptes multi-opérateurs
* API publique mobilité
* IA auto-adaptative

---

# 👨‍💻 Auteurs

### 👤 Amine Chachou

### 👤 Christ MVE

Projet réalisé dans le cadre du développement d’une plateforme intelligente de supervision des mobilités urbaines.

---

# ⚠️ Important

Le projet est actuellement un **prototype avancé V5** destiné à démontrer :

* la faisabilité technique
* l’intégration IA + Open Data
* la supervision temps réel
* la prédiction des flux urbains

Les données d’affluence restent partiellement simulées pour le prototypage.

---

# 🚇 PredicTrafic IA

### *“Predict mobility before congestion happens.”*
