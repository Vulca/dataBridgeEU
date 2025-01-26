import psycopg2
from flask import Flask

app = Flask(__name__)

# Configuration de la base de données
DATABASE_CONFIG = {
    "dbname": "makertour_funds",  # Nom de votre base
    "user": "databridgeeu_user",          # Nom d'utilisateur
    "password": "UJSsl11OhPeLP6BSVvRAZ76MnSsEGGtT",      # Mot de passe
    "host": "dpg-cub4952n91rc7390ja7g-a",         # Adresse du serveur Render
    "port": "5432"               # Port par défaut
}

# Connexion à PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DATABASE_CONFIG["dbname"],
        user=DATABASE_CONFIG["user"],
        password=DATABASE_CONFIG["password"],
        host=DATABASE_CONFIG["host"],
        port=DATABASE_CONFIG["port"]
    )
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")  # Simple requête pour tester
    result = cur.fetchone()
    conn.close()
    return f"Database connected: {result}"