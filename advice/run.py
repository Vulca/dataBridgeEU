import sys
print(sys.path)
import os

# Ajouter le chemin du répertoire racine au chemin de recherche
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app

# Crée une instance de l'application Flask
app = create_app()

if __name__ == "__main__":
    # Lance le serveur Flask
    app.run(debug=True)
