from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import logging
import traceback
import os

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Obtenir le chemin absolu du fichier modèle
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'best_heart_model.joblib')
logger.info(f"Chemin du modèle: {model_path}")

# Charger le modèle sauvegardé
try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Le fichier modèle n'existe pas à l'emplacement: {model_path}")
    
    model = joblib.load(model_path)
    logger.info("Modèle chargé avec succès")
except Exception as e:
    logger.error(f"Erreur lors du chargement du modèle: {str(e)}")
    raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logger.debug(f"Données reçues: {data}")
        
        # Vérifier si toutes les données nécessaires sont présentes
        required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                         'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        
        for field in required_fields:
            if field not in data:
                logger.error(f"Champ manquant: {field}")
                return jsonify({'error': f'Le champ {field} est manquant'}), 400
        
        # Convertir les données en nombres
        try:
            features = np.array([
                float(data['age']), float(data['sex']), float(data['cp']),
                float(data['trestbps']), float(data['chol']), float(data['fbs']),
                float(data['restecg']), float(data['thalach']), float(data['exang']),
                float(data['oldpeak']), float(data['slope']), float(data['ca']),
                float(data['thal'])
            ]).reshape(1, -1)
            logger.debug(f"Features préparées: {features}")
        except ValueError as e:
            logger.error(f"Erreur de conversion des données: {str(e)}")
            return jsonify({'error': 'Toutes les valeurs doivent être numériques'}), 400

        # Faire la prédiction
        try:
            prediction = model.predict(features)
            probability = model.predict_proba(features)[0]
            logger.info(f"Prédiction réussie: {prediction[0]}, Probabilité: {probability[1]}")
            
            return jsonify({
                'Heart Disease Prediction': int(prediction[0]),
                'Probability': float(probability[1])
            })
        except Exception as e:
            logger.error(f"Erreur lors de la prédiction: {str(e)}")
            logger.error(traceback.format_exc())
            return jsonify({'error': f'Erreur lors de la prédiction: {str(e)}'}), 500
        
    except Exception as e:
        logger.error(f"Erreur générale: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': 'Une erreur est survenue lors de la prédiction'}), 500

if __name__ == '__main__':
    app.run(debug=True) 