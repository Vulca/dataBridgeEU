import os
from supabase import create_client, Client

# Charger les variables d'environnement

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Connexion réussie à Supabase !")
