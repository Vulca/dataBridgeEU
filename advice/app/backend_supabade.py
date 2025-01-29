from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Les variables SUPABASE_URL et SUPABASE_KEY doivent être définies dans le fichier .env.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app = FastAPI()

# Modèles
class DataModel(BaseModel):
    table: str
    data: dict

class UpdateModel(BaseModel):
    table: str
    id_field: str
    id_value: str
    data: dict

# Routes
@app.post("/add/")
def add_data(payload: DataModel):
    try:
        response = supabase.table(payload.table).insert(payload.data).execute()
        return {"message": "Données ajoutées", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/update/")
def update_data(payload: UpdateModel):
    try:
        response = supabase.table(payload.table).update(payload.data).eq(payload.id_field, payload.id_value).execute()
        return {"message": "Données mises à jour", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/get/{table}")
def get_data(table: str, filters: str = None, limit: int = 10, offset: int = 0):
    try:
        query = supabase.table(table).select("*").range(offset, offset + limit - 1)
        if filters:
            key, value = filters.split("=")
            query = query.eq(key, value)
        response = query.execute()
        return {"data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tables/")
def get_tables():
    try:
        tables = ["users", "products", "orders"]  # Dynamique si possible
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete/{table}/{id}")
def delete_data(table: str, id: int):
    try:
        response = supabase.table(table).delete().eq("id", id).execute()
        return {"message": "Donnée supprimée", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
