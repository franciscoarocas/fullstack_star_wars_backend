
from fastapi import FastAPI

from .routers import all_routes

from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

import os

load_dotenv()

app = FastAPI()

origins = os.getenv("CORS_ORIGINS", '').split(",")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registration of all routers
for router in all_routes:
    app.include_router(router)

if __name__ == "__main__":

    host = os.getenv("HOST", None)
    port = int(os.getenv("PORT", 80))
    reload = os.getenv("RELOAD", "false").lower() == "true"

    import uvicorn
    uvicorn.run("main:app", host=host, port=port, reload=reload)