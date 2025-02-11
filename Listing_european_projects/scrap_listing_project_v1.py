from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 📌 Définir le chemin de téléchargement
download_dir = "/Users/Photographe/Documents/4_Organisations/03. Vulca/Listing projets européens/Codes/DataBridgeEu/Listing_european_projects/extract"

# 📌 Configurer Firefox
firefox_options = Options()
firefox_options.set_preference("browser.download.folderList", 2)  # Emplacement personnalisé
firefox_options.set_preference("browser.download.dir", download_dir)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
firefox_options.set_preference("pdfjs.disabled", True)  # Désactiver l'ouverture automatique des PDF

# 📌 Lancer Firefox
driver = webdriver.Firefox(options=firefox_options)

# 📌 Ouvrir la page
url = "https://erasmus-plus.ec.europa.eu/projects/search/"
driver.get(url)

# 📌 Attendre que la page charge complètement
wait = WebDriverWait(driver, 10)

# 📌 Attendre que la barre de recherche soit bien visible et interactive
search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder=' Example: university, school, etc.']")))

# ✅ Vérification : Afficher un message si l'élément est bien détecté
print("✅ Barre de recherche trouvée.")

# 📌 Effacer le champ avant d'écrire pour éviter d'éventuels problèmes
search_box.clear()
time.sleep(1)

# 📌 Entrer le nom de l'organisation
search_box.send_keys("Buinho Associação")
time.sleep(1)  # Petite pause pour bien voir le texte s'afficher

# ✅ Vérification : Afficher ce qui a été écrit
print("✍️ Texte écrit dans la barre de recherche.")

# 📌 Appuyer sur Entrée pour valider la recherche
search_box.send_keys(Keys.RETURN)

# 📌 Attendre que les résultats apparaissent
time.sleep(5)

# 📌 Vérifier si le bouton "Export XLS" est bien présent
xls_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download results (XLS)')]")))

# ✅ Vérification : Afficher un message si le bouton est trouvé
print("✅ Bouton Export XLS trouvé.")

# 📌 Cliquer sur le bouton "Export XLS"
xls_button.click()

# 📌 Attendre le téléchargement du fichier
time.sleep(10)  # Ajuster selon la rapidité du téléchargement

# 📌 Vérifier si le fichier a bien été téléchargé
files = os.listdir(download_dir)
xls_files = [f for f in files if f.endswith(".xls")]

if xls_files:
    print(f"✅ Fichier téléchargé : {xls_files[0]}")
else:
    print("❌ Aucun fichier XLS téléchargé.")

# 📌 Fermer Firefox
driver.quit()
