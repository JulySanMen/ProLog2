from flask import Flask, request, jsonify
from gridsearch import perform_grid_search  # Importar la función de model.py

app = Flask(__name__)

@app.route('/')
def home():
    return "API de búsqueda de hiperparámetros está activa."

@app.route('/gridsearch', methods=['POST'])
def grid_search():
    try:
        # Llamar a la función del modelo para realizar la búsqueda
        top_results = perform_grid_search()
        return jsonify(top_results)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main...':
    app.run(debug=True)
