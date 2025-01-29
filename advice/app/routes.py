from flask import Blueprint, render_template, request, jsonify
from .supabase_client import insert_data
from app.supabase_client import fetch_graph_data


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('Data_update.html')

@main.route('/add-data', methods=['POST'])
def add_data():
    data = request.form.to_dict()
    response = insert_data(data)  # Appelle ta fonction Supabase
    return jsonify({"success": response})

@main.route('/fetch-dashboard-data', methods=['GET'])
def fetch_dashboard_data():
    data = fetch_graph_data()  # Récupère des données depuis Supabase pour les graphiques
    return jsonify(data)
