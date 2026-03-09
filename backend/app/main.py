
from fastapi import FastAPI
from .routes import wallet
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(wallet.router)

@app.get("/")
def root():
    return {"wallet":"running"}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=port)
