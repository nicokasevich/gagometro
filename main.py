from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin, ModelView

from core import database
from endpoints.players import router as players_router
from models.player import Player


def create_app() -> FastAPI:
    app = FastAPI()

    database.Base.metadata.create_all(bind=database.engine)

    app.include_router(players_router)

    admin = Admin(database.engine, title="Admin Panel")
    admin.add_view(ModelView(Player))

    admin.mount_to(app)

    return app
