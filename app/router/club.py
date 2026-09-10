from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schema.club import ClubSchema
from app.service.club_service import ClubService


router = APIRouter(
    prefix="/clubs",
    tags=["Clubs"]
)


@router.post(
    "/",
    response_model=ClubSchema,
    status_code=status.HTTP_201_CREATED
)
def create_club(
    club_data: ClubSchema,
    db: Session = Depends(get_db)
):
    service = ClubService(db)

    return service.create_club(club_data)


@router.get(
    "/",
    response_model=list[ClubSchema]
)
def get_all_clubs(
    db: Session = Depends(get_db)
):
    service = ClubService(db)

    return service.get_all_clubs()


@router.get(
    "/{club_id}",
    response_model=ClubSchema
)
def get_club(
    club_id: int,
    db: Session = Depends(get_db)
):
    service = ClubService(db)

    club = service.get_club(club_id)

    if club is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Club not found"
        )

    return club


@router.put(
    "/{club_id}",
    response_model=ClubSchema
)
def update_club(
    club_id: int,
    club_data: ClubSchema,
    db: Session = Depends(get_db)
):
    service = ClubService(db)

    club = service.update_club(club_id, club_data)

    if club is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Club not found"
        )

    return club


@router.delete(
    "/{club_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_club(
    club_id: int,
    db: Session = Depends(get_db)
):
    service = ClubService(db)

    deleted = service.delete_club(club_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Club not found"
        )

    return None