import requests

organisation_name = "Buinho Associação"
search_url = "https://webgate.ec.europa.eu/erasmus-esc/index/organisations/search-for-an-organisation"

params = {
    "organisationName": organisation_name
}

response = requests.get(search_url, params=params)

print("Statut de la réponse :", response.status_code)
print("Contenu de la réponse :", response.text)  # Afficher les 500 premiers caractères
