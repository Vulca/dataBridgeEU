import requests

from bs4 import BeautifulSoup

# URL de la page de recherche
search_url = 'https://webgate.ec.europa.eu/erasmus-esc/index/organisations/search-for-an-organisation'

# Fonction pour rechercher une organisation et extraire son OID
def get_organisation_oid(organisation_name):
    # Données du formulaire de recherche
    data = {
        'organisationName': organisation_name,
        # Ajoutez d'autres paramètres si nécessaire
    }
    
    # Effectuer la requête POST
    response = requests.post(search_url, data=data)
    print(response)
    # Analyser la réponse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Rechercher l'élément contenant l'OID (à adapter en fonction de la structure HTML)
    oid_element = soup.find('a', {'class': 'organisation-link'})
    
    if oid_element:
        oid = oid_element.get('href').split('/')[-1]  # Extraire l'OID de l'URL
        return oid
    else:
        return None

# Exemple d'utilisation
organisation_name = 'Buinho Associação'
oid = get_organisation_oid(organisation_name)
if oid:
    print(f'OID de {organisation_name} : {oid}')
else:
    print(f'Organisation {organisation_name} non trouvée.')
