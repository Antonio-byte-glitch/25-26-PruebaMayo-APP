from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)


# Código que se añade
@app.get("/status")
def version():
    return {"status": "P4z0_P0rr4S, 4nt0ni0 - v.xx"}
