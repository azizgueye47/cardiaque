import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    # Charger les données
    logger.info("Chargement des données...")
    df = pd.read_csv('heart (1).csv')
    logger.info(f"Données chargées: {len(df)} lignes")

    # Préparer les features et la target
    X = df.drop('target', axis=1)
    y = df['target']
    logger.info(f"Features: {X.shape}, Target: {y.shape}")

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logger.info(f"Ensemble d'entraînement: {X_train.shape}, Ensemble de test: {X_test.shape}")

    # Créer et entraîner le modèle
    logger.info("Création et entraînement du modèle...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    logger.info("Modèle entraîné avec succès")

    # Évaluer le modèle
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Accuracy: {accuracy:.2f}")

    # Vérifier que le modèle a la méthode predict
    if hasattr(model, 'predict'):
        logger.info("Le modèle a la méthode predict")
    else:
        raise AttributeError("Le modèle n'a pas la méthode predict")

    # Sauvegarder le modèle avec joblib
    logger.info("Sauvegarde du modèle...")
    joblib.dump(model, 'best_heart_model.joblib')
    logger.info("Modèle sauvegardé avec succès dans 'best_heart_model.joblib'")

    # Vérifier que le modèle peut être rechargé
    logger.info("Vérification du modèle sauvegardé...")
    loaded_model = joblib.load('best_heart_model.joblib')
    if hasattr(loaded_model, 'predict'):
        logger.info("Le modèle rechargé a la méthode predict")
        # Tester une prédiction
        test_pred = loaded_model.predict(X_test[:1])
        logger.info(f"Test de prédiction réussi: {test_pred[0]}")
    else:
        raise AttributeError("Le modèle rechargé n'a pas la méthode predict")

except Exception as e:
    logger.error(f"Erreur: {str(e)}")
    raise 