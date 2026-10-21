from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Trading Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Ganti pakai * biar frontend bisa akses
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "AI Trading Assistant API aktif",
        "ai_connected": False,
        "trading_enabled": False,
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
