from urllib.parse import quote

def quote_url(url: str) -> str:
    """
    Encode une URL en échappant les caractères spéciaux.
    """
    return quote(url, safe="")

def format_date(date):
    """Formatte une date au format 'YYYY-MM-DD'."""
    return date.strftime('%Y-%m-%d')

def validate_input(data, required_fields):
    """Valide que les champs requis sont présents dans les données."""
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Champs manquants : {', '.join(missing_fields)}")
    return True
