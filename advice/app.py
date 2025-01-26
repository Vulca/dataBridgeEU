import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    except Exception as e:
        print("Erreur lors de la connexion à la base de données :", e)
        raise

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")  # Exemple de requête
        return "Connexion réussie à la base de données !"
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
