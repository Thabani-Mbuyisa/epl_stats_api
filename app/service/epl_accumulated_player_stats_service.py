from sqlalchemy.orm import Session

from app.model.epl_accumulated_player_stats import EplAccumulatedPlayerStats
from app.schema.epl_accumulated_player_stats import EplAccumulatedPlayerStatsSchema


class EplAccumulatedPlayerStatsService:

    def __init__(self, db: Session):
        self.db = db

    def create_stats(
        self,
        stats_data: EplAccumulatedPlayerStatsSchema
    ) -> EplAccumulatedPlayerStats:

        stats = EplAccumulatedPlayerStats(
            **stats_data.model_dump()
        )

        self.db.add(stats)
        self.db.commit()
        self.db.refresh(stats)

        return stats

    def get_all_acc_stats(
    self,
    season_id: int
    ) -> list[EplAccumulatedPlayerStats]:

        return (
            self.db
            .query(EplAccumulatedPlayerStats)
            .filter(
                EplAccumulatedPlayerStats.season_id == season_id
            )
            .all()
        )

    def get_acc_stats_by_player(
        self,
        player_id: int,
        season_id: int
    ) -> EplAccumulatedPlayerStats | None:

        return (
            self.db.query(EplAccumulatedPlayerStats)
            .filter(
                EplAccumulatedPlayerStats.id == player_id,
                EplAccumulatedPlayerStats.season_id == season_id
            )
            .first()
        )

    def get_acc_stats_by_team(
        self,
        team_id: int,
        season_id: int
    ) -> list[EplAccumulatedPlayerStats]:

        return (
            self.db.query(EplAccumulatedPlayerStats)
            .filter(
                EplAccumulatedPlayerStats.team_id == team_id,
                EplAccumulatedPlayerStats.season_id == season_id
            )
            .all()
        )
    
    def update_stats(
        self,
        player_id: int,
        season_id: int,
        stats_data: EplAccumulatedPlayerStatsSchema
    ) -> EplAccumulatedPlayerStats | None:

        stats = (
            self.db
            .query(EplAccumulatedPlayerStats)
            .filter(
                EplAccumulatedPlayerStats.id == player_id,
                EplAccumulatedPlayerStats.season_id == season_id
            )
            .first()
        )

        if stats is None:
            return None

        for field, value in stats_data.model_dump().items():
            setattr(stats, field, value)

        self.db.commit()
        self.db.refresh(stats)

        return stats
    
    def delete_stats(
        self,
        player_id: int,
        season_id: int
    ) -> bool:

        stats = (
            self.db
            .query(EplAccumulatedPlayerStats)
            .filter(
                EplAccumulatedPlayerStats.id == player_id,
                EplAccumulatedPlayerStats.season_id == season_id
            )
            .first()
        )

        if stats is None:
            return False

        self.db.delete(stats)
        self.db.commit()

        return True