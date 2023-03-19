from fastapi import FastAPI
from config import settings
from database import engine
from models import Base
from routers import users, items


Base.metadata.create_all(bind=engine)

tags = [
    {
        "name": "user",
        "description": "user routes"
    },
    {
        "name": "item",
        "description": "item routes"
    }
]


app = FastAPI(
                title=settings.TITLE,
                description=settings.DECRIPTION, version=settings.VERSION,
                contact={"name": settings.NAME,
                         "email": settings.EMAIL
                        },
                openapi_tags=tags,
                openapi_url="/api/v1/openapi.json",
                docs_url="/docs",
                redoc_url=None
            )

app.include_router(users.router)
app.include_router(items.router)