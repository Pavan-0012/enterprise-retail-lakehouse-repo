from fastapi import FastAPI

from seed.api.routes import router

app = FastAPI(
    title="Enterprise Retail Source API",
    version="1.0.0",
)

app.include_router(router)