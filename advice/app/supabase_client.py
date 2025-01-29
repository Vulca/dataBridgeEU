import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Charger les variables d'environnement
load_dotenv()

# Récupérer les URL et clé d'accès de Supabase depuis .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Vérifier que les variables sont définies
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Les variables SUPABASE_URL et SUPABASE_KEY doivent être définies dans le fichier .env.")

# Créer le client Supabase
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    raise ConnectionError(f"Erreur lors de la connexion à Supabase : {e}")


def insert_data(table_name: str, data: dict) -> bool:
    """
    Insère des données dans une table spécifique de Supabase.
    
    Args:
        table_name (str): Nom de la table dans Supabase.
        data (dict): Données à insérer sous forme de dictionnaire.

    Returns:
        bool: True si l'insertion réussit, False sinon.
    """
    try:
        response = supabase.table(table_name).insert(data).execute()
        return response.status_code == 200
    except Exception as e:
        print(f"Erreur lors de l'insertion des données dans la table {table_name}: {e}")
        return False

def fetch_graph_data() -> list:
    """
    Récupère les données nécessaires pour les graphiques depuis Supabase.

    Returns:
        list: Liste de données pour les graphiques.
    """
    try:
        response = supabase.table("graph_data").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        print(f"Erreur lors de la récupération des données graphiques : {e}")
        return []

def update_data(table_name: str, filters: dict, updates: dict) -> bool:
    """
    Met à jour des données dans une table spécifique de Supabase.

    Args:
        table_name (str): Nom de la table dans Supabase.
        filters (dict): Filtres pour identifier les lignes à mettre à jour.
        updates (dict): Valeurs à mettre à jour.

    Returns:
        bool: True si la mise à jour réussit, False sinon.
    """
    try:
        query = supabase.table(table_name).update(updates)
        for key, value in filters.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.status_code == 200
    except Exception as e:
        print(f"Erreur lors de la mise à jour des données dans la table {table_name}: {e}")
        return False


def delete_data(table_name: str, filters: dict) -> bool:
    """
    Supprime des données dans une table spécifique de Supabase.

    Args:
        table_name (str): Nom de la table dans Supabase.
        filters (dict): Filtres pour identifier les lignes à supprimer.

    Returns:
        bool: True si la suppression réussit, False sinon.
    """
    try:
        query = supabase.table(table_name).delete()
        for key, value in filters.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.status_code == 200
    except Exception as e:
        print(f"Erreur lors de la suppression des données dans la table {table_name}: {e}")
        return False
