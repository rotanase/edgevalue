from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Dividend])
def read_dividends(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve dividends.
    """
    dividends = crud.dividend.get_multi(db, skip=skip, limit=limit)
    return dividends


@router.post("/", response_model=schemas.Dividend)
def create_dividend(
    *,
    db: Session = Depends(deps.get_db),
    dividend_in: schemas.DividendCreate,
) -> Any:
    """
    Create new dividend.
    """
    dividend = crud.dividend.create(db=db, obj_in=dividend_in)
    return dividend


@router.put("/{id}", response_model=schemas.Dividend)
def update_dividend(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    dividend_in: schemas.DividendUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a dividend.
    """
    dividend = crud.dividend.get(db=db, id=id)
    if not dividend:
        raise HTTPException(status_code=404, detail="Dividend not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    dividend = crud.dividend.update(db=db, db_obj=dividend, obj_in=dividend_in)
    return dividend


@router.get("/{id}", response_model=schemas.Dividend)
def read_dividend(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get dividend by ID.
    """
    dividend = crud.dividend.get(db=db, id=id)
    if not dividend:
        raise HTTPException(status_code=404, detail="Dividend not found")
    return dividend


@router.delete("/{id}", response_model=schemas.Dividend)
def delete_dividend(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a dividend.
    """
    dividend = crud.dividend.get(db=db, id=id)
    if not dividend:
        raise HTTPException(status_code=404, detail="Dividend not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    dividend = crud.dividend.remove(db=db, id=id)
    return dividend
