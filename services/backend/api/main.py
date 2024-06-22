from fastapi import FastAPI

from api.connection import prisma_connection
from api.routers import user

app = FastAPI(lifespan=prisma_connection.lifespan)

app.include_router(
    user.router,
    prefix="/user",
    tags=["User"],
)