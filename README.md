# Prédiction de Maladie Cardiaque

Une application web de prédiction de maladie cardiaque utilisant l'intelligence artificielle. Cette application permet aux utilisateurs de prédire le risque de maladie cardiaque en fonction de divers paramètres médicaux.

## Fonctionnalités

- Interface utilisateur moderne et intuitive
- Formulaire interactif pour saisir les données du patient
- Prédiction en temps réel
- Visualisation des probabilités
- Design responsive (mobile et desktop)

## Technologies Utilisées

- Python
- Flask
- Scikit-learn
- Bootstrap 5
- HTML5/CSS3
- JavaScript

## Installation Locale

1. Clonez le repository :
```bash
git clone https://github.com/azizgueye47/cardiaque.git
cd cardiaque
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancez l'application :
```bash
python app.py
```

5. Accédez à l'application :
```
http://localhost:5000
```

## Déploiement sur Render.com

1. Créez un compte sur [Render.com](https://render.com)

2. Connectez votre compte GitHub

3. Créez un nouveau Web Service :
   - Cliquez sur "New +" et sélectionnez "Web Service"
   - Connectez votre repository GitHub
   - Configurez le service :
     ```
     Name: heart-disease-prediction
     Environment: Python
     Build Command: pip install -r requirements.txt
     Start Command: gunicorn app:app
     ```

4. Cliquez sur "Create Web Service"

## Utilisation

1. Accédez à l'application via l'URL fournie par Render
2. Remplissez le formulaire avec les informations du patient
3. Cliquez sur "Prédire" pour obtenir la prédiction
4. Consultez les résultats et les probabilités

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 
