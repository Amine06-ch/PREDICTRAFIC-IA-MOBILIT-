import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib
import os

print("🧠 Lancement du processus d'apprentissage Machine Learning...")


df = pd.read_csv('data/dataset_complet.csv')

df_global = df.groupby(['Heure', 'Jour', 'Meteo'])['Affluence'].mean().reset_index()

X = pd.get_dummies(df_global[['Heure', 'Jour', 'Meteo']], drop_first=True)
y = df_global['Affluence']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42)
model.fit(X_train, y_train)


score = r2_score(y_test, model.predict(X_test)) * 100
print(f"📊 Validation du modèle IA | Score de Précision (R²) : {score:.1f}%")


os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/rf_model.pkl')
joblib.dump(list(X.columns), 'models/features.pkl')

print("✅ Cerveau IA compilé et sauvegardé dans le dossier 'models/'. Prêt pour la production !")