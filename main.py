from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os, httpx

load_dotenv(dotenv_path=".env", override=True)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL ou SUPABASE_KEY manquant dans .env")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← autorise les requêtes cross-origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/articles")
async def get_all_articles():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"{SUPABASE_URL}/rest/v1/DzawTable1",
                headers={
                    "apikey": SUPABASE_KEY,
                    "Authorization": f"Bearer {SUPABASE_KEY}"
                },
                params={"select": "*", "order": "created_at.asc"}
            )
            res.raise_for_status()
            return res.json()
    except Exception as e:
        raise HTTPException(500, f"Erreur Supabase : {e}")

@app.post("/article")
async def insert_article(article: dict):
    print("DEBUG >>> article reçu :", article)  # 👈 Ajoute cette ligne
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{SUPABASE_URL}/rest/v1/DzawTable1",  # ← Vérifie bien ce nom
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json"
            },
            json=article
        )
        res.raise_for_status()
        return {"ok": True}
# @app.post("/article")
# async def insert_article(article: dict):
#     async with httpx.AsyncClient() as client:
#         res = await client.post(
#             f"{SUPABASE_URL}/rest/v1/articles",
#             headers={
#                 "apikey": SUPABASE_KEY,
#                 "Authorization": f"Bearer {SUPABASE_KEY}",
#                 "Content-Type": "application/json"
#             },
#             json=article
#         )
#         res.raise_for_status()
#         return {"ok": True}