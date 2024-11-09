from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Utilisez votre modèle d'IA pour faire une prédiction
    # Exemple : prediction = votre_modele.predict(data)
    prediction = {"example_prediction": 42}  # Remplacez par votre logique de prédiction
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)