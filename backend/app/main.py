
from fastapi import FastAPI
from .routes import wallet
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(wallet.router)

@app.get("/")
def root():
    return {"wallet":"running"}
