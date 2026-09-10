from sqlalchemy.orm import Session

from app.model.club import Club
from app.schema.club import ClubSchema


class ClubService:

    def __init__(self, db: Session):
        self.db = db

    def create_club(self, club_data: ClubSchema) -> Club:
        club = Club(
            id=club_data.id,
            name=club_data.name,
            short_name=club_data.short_name,
            abbr=club_data.abbr,
            stadium_name=club_data.stadium_name,
            stadium_city=club_data.stadium_city,
            stadium_country=club_data.stadium_country,
            stadium_capacity=club_data.stadium_capacity
        )

        self.db.add(club)
        self.db.commit()
        self.db.refresh(club)

        return club

    def get_club(self, club_id: int) -> Club | None:
        return (
            self.db.query(Club)
            .filter(Club.id == club_id)
            .first()
        )

    def get_all_clubs(self) -> list[Club]:
        return self.db.query(Club).all()

    def update_club(
        self,
        club_id: int,
        club_data: ClubSchema
    ) -> Club | None:

        club = (
            self.db.query(Club)
            .filter(Club.id == club_id)
            .first()
        )

        if club is None:
            return None

        club.name = club_data.name
        club.short_name = club_data.short_name
        club.abbr = club_data.abbr
        club.stadium_name = club_data.stadium_name
        club.stadium_city = club_data.stadium_city
        club.stadium_country = club_data.stadium_country
        club.stadium_capacity = club_data.stadium_capacity

        self.db.commit()
        self.db.refresh(club)

        return club

    def delete_club(self, club_id: int) -> bool:

        club = (
            self.db.query(Club)
            .filter(Club.id == club_id)
            .first()
        )

        if club is None:
            return False

        self.db.delete(club)
        self.db.commit()

        return True