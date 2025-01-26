import os
import psycopg2
from flask import Flask
import logging

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default-secret-key")

logging.basicConfig(level=logging.INFO)

DATABASE_CONFIG = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT", 5432),  # 5432 par défaut
}

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DATABASE_CONFIG["dbname"],
            user=DATABASE_CONFIG["user"],
            password=DATABASE_CONFIG["password"],
            host=DATABASE_CONFIG["host"],
            port=DATABASE_CONFIG["port"],
        )
        return conn
    except psycopg2.OperationalError as e:
        logging.error(f"Erreur de connexion à la base de données : {e}")
        return None

@app.route("/")
def home():
    logging.info("Requête reçue sur /")
    conn = get_db_connection()
    if conn is None:
        logging.error("Erreur de connexion à la base de données")
        return "Impossible de se connecter à la base de données", 500
    cur = conn.cursor()
    cur.execute("SELECT 'Bienvenue !'")
    result = cur.fetchone()
    conn.close()
    logging.info("Requête réussie")
    return result[0]

if __name__ == "__main__":
    # Récupérer le port de l'environnement ou utiliser 5000 par défaut
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
