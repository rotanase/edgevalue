from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DailyRatio])
def read_daily_ratios(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve daily ratios.
    """
    daily_ratios = crud.daily_ratio.get_multi(db, skip=skip, limit=limit)
    return daily_ratios


@router.post("/", response_model=schemas.DailyRatio)
def create_daily_ratio(
    *,
    db: Session = Depends(deps.get_db),
    daily_ratio_in: schemas.DailyRatioCreate,
) -> Any:
    """
    Create new daily ratio.
    """
    daily_ratio = crud.daily_ratio.create(db=db, obj_in=daily_ratio_in)
    return daily_ratio


@router.put("/{id}", response_model=schemas.DailyRatio)
def update_daily_ratio(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    daily_ratio_in: schemas.DailyRatioUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a daily ratio.
    """
    daily_ratio = crud.daily_ratio.get(db=db, id=id)
    if not daily_ratio:
        raise HTTPException(status_code=404, detail="Daily ratio not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    daily_ratio = crud.daily_ratio.update(db=db, db_obj=daily_ratio, obj_in=daily_ratio_in)
    return daily_ratio


@router.get("/{id}", response_model=schemas.DailyRatio)
def read_daily_ratio(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get daily ratio by ID.
    """
    daily_ratio = crud.daily_ratio.get(db=db, id=id)
    if not daily_ratio:
        raise HTTPException(status_code=404, detail="Daily ratio not found")
    return daily_ratio


@router.delete("/{id}", response_model=schemas.DailyRatio)
def delete_daily_ratio(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a daily ratio.
    """
    daily_ratio = crud.daily_ratio.get(db=db, id=id)
    if not daily_ratio:
        raise HTTPException(status_code=404, detail="Daily ratio not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    daily_ratio = crud.daily_ratio.remove(db=db, id=id)
    return daily_ratio
