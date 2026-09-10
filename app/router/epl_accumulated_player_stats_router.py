from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schema.epl_accumulated_player_stats import EplAccumulatedPlayerStatsSchema
from app.service.epl_accumulated_player_stats_service import EplAccumulatedPlayerStatsService



router = APIRouter(
    prefix="/epl/accumulated-player-stats",
    tags=["EPL Accumulated Player Stats"]
)


@router.get(
    "/season/{season_id}",
    response_model=list[EplAccumulatedPlayerStatsSchema]
)
def get_all_acc_stats(
    season_id: int,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    return service.get_all_acc_stats(season_id)


@router.get(
    "/player/{player_id}/season/{season_id}",
    response_model=EplAccumulatedPlayerStatsSchema
)
def get_stats_by_player(
    player_id: int,
    season_id: int,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    stats = service.get_stats_by_player(
        player_id,
        season_id
    )

    if stats is None:
        raise HTTPException(
            status_code=404,
            detail="Player statistics not found"
        )

    return stats


@router.get(
    "/team/{team_id}/season/{season_id}",
    response_model=list[EplAccumulatedPlayerStatsSchema]
)
def get_stats_by_team(
    team_id: int,
    season_id: int,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    return service.get_stats_by_team(
        team_id,
        season_id
    )


@router.post(
    "/",
    response_model=EplAccumulatedPlayerStatsSchema
)
def create_acc_stats(
    stats_data: EplAccumulatedPlayerStatsSchema,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    return service.create_stats(stats_data)


@router.put(
    "/player/{player_id}/season/{season_id}",
    response_model=EplAccumulatedPlayerStatsSchema
)
def update_acc_stats(
    player_id: int,
    season_id: int,
    stats_data: EplAccumulatedPlayerStatsSchema,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    stats = service.update_stats(
        player_id,
        season_id,
        stats_data
    )

    if stats is None:
        raise HTTPException(
            status_code=404,
            detail="Player statistics not found"
        )

    return stats


@router.delete(
    "/player/{player_id}/season/{season_id}"
)
def delete_acc_stats(
    player_id: int,
    season_id: int,
    db: Session = Depends(get_db)
):
    service = EplAccumulatedPlayerStatsService(db)

    deleted = service.delete_stats(
        player_id,
        season_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Player statistics not found"
        )

    return {
        "message": "Player statistics deleted successfully"
    }