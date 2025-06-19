
from typing import Union

from fastapi import FastAPI

from .routers import all_routes

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Registration of all routers
for router in all_routes:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)