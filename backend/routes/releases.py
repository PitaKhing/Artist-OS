from pydantic import BaseModel
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
import models
from fastapi import HTTPException

router = APIRouter()


class ReleaseCreate(BaseModel):
    title: str
    artist: str
    status: str


@router.get("/releases")
def get_releases(db: Session = Depends(get_db)):
    return db.query(models.Release).all()

@router.put("/releases/{release_id}")
def update_release(
    release_id: int, 
    release: ReleaseCreate,
    db: Session = Depends(get_db)
):
    db_release = db.query(models.Release).filter(
        models.Release.id == release_id
    ).first()

    if db_release is None:
        raise HTTPException(
            status_code=404,
            detail="Release not found"
        )
    
    db_release.title = release.title
    db_release.artist = release.artist
    db_release.status = release.status

    db.commit()
    db.refresh(db_release)
    
    return db_release

@router.delete("/releases/{release_id}")
def delete_release(
    release_id: int,
    db: Session = Depends(get_db)
):
    release = db.query(models.Release).filter(
        models.Release.id == release_id
    ).first()

    if release is None:
        raise HTTPException(
            status_code=404,
            detail="Release not found"
        )
    
    db.delete(release)
    db.commit()

    return {"message": "Release deleted successfully"}

@router.post("/releases")
def create_release(
    release: ReleaseCreate,
    db: Session = Depends(get_db)
):
    db_releases = models.Release(
        title=release. title,
        status=release. status
    )

    db.add(db_releases)
    db.commit()
    db.refresh(db_releases)
    
    return db_releases