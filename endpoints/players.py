from fastapi import APIRouter, Depends, HTTPException

from repositories.player import PlayerRepository
from schemas.player import PlayerSchema, PlayerUpdate

router = APIRouter()


@router.get("/players")
def get_players(player_repository: PlayerRepository = Depends()) -> list[PlayerSchema]:
    return player_repository.get_players()


@router.get("/players/{player_id}")
def get_player(
    player_id: int, player_repository: PlayerRepository = Depends()
) -> PlayerSchema:
    player = player_repository.get_player(player_id)

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@router.patch("/players/{player_id}")
def update_player(
    player_id: int,
    player: PlayerUpdate,
    player_repository: PlayerRepository = Depends(),
) -> PlayerSchema:
    player = player_repository.get_player(player_id)

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player_repository.update_player(player_id, player)
