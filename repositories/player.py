from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from models.player import Player
from schemas.player import PlayerUpdate


class PlayerRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_players(self) -> list[Player]:
        return self.db.query(Player).all()

    def get_player(self, player_id: int) -> Optional[Player]:
        return self.db.query(Player).filter(Player.id == player_id).first()

    def update_player(self, player_id: int, player: PlayerUpdate) -> Player:
        self.db.query(Player).filter(Player.id == player_id).update(player.model_dump())
        return self.db.query(Player).filter(Player.id == player_id).first()
