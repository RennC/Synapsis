from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth_router, paths_router

app = FastAPI(title="CognitaPath API")

# Configuração do CORS para permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja para o domínio do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(paths_router.router, prefix="/api/v1/paths", tags=["paths"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the CognitaPath API"}
