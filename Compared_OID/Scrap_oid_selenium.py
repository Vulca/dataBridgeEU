from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_organisation_info(organisation_name):
    """ Recherche une organisation Erasmus+ et extrait son OID et son PIC """

    # 🔹 Configuration de Selenium avec Firefox
    GECKODRIVER_PATH = "/usr/local/bin/geckodriver"  # Adapter selon ton installation
    firefox_options = Options()
    # firefox_options.add_argument("--headless")  # Décommente si tu veux voir la page en live

    # 🔹 Lancement du WebDriver
    service = Service(GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        # 🔹 Charger la page de recherche
        url = "https://webgate.ec.europa.eu/erasmus-esc/index/organisations/search-for-an-organisation"
        driver.get(url)

        # ✅ Attendre que le champ de recherche soit visible
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control"))
        )
        print("✅ Le champ de recherche est visible.")

        # ✅ Taper l'organisation lettre par lettre
        search_box.clear()
        for letter in organisation_name:
            search_box.send_keys(letter)
            time.sleep(0.2)  # Pause courte entre chaque lettre

        print("✅ Nom tapé entièrement, attente des résultats...")

        # ✅ Attendre que les suggestions apparaissent
        time.sleep(2)  # Attente pour éviter une recherche trop rapide

        # ✅ Attendre que le bouton de recherche soit cliquable avant de cliquer
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ux-field-search__search-button"))
        )
        search_button.click()

        print("✅ Recherche lancée, attente des résultats...")

        # ✅ Attendre que les résultats soient chargés
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ux-layout-page-column__body-content"))
        )

        # ✅ Vérifier si l'organisation est bien affichée
        org_card = driver.find_element(By.CSS_SELECTOR, ".ux-card__header-title-main span")
        org_name = org_card.text.strip()
        print(f"✅ Organisation trouvée : {org_name}")

        # ✅ Extraire l’OID
        oid_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Organisation ID')]/strong")
        oid = oid_element.text.strip()
        print(f"📌 OID trouvé : {oid}")

        # ✅ Extraire le PIC
        pic_element = driver.find_element(By.XPATH, "//span[contains(text(), 'PIC')]/strong")
        pic = pic_element.text.strip()
        print(f"📌 PIC trouvé : {pic}")

        return {"Organisation": org_name, "OID": oid, "PIC": pic}

    except Exception as e:
        print("⚠️ Erreur :", e)
        return None

    finally:
        driver.quit()

# 🔥 Test du script avec une organisation
if __name__ == "__main__":
    organisation_a_tester = "Buinho Associação"
    result = get_organisation_info(organisation_a_tester)
    if result:
        print("\n🎯 Résultat final :", result)
