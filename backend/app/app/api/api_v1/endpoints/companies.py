from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Company])
def read_companies(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve companies.
    """
    companies = crud.company.get_multi(db, skip=skip, limit=limit)
    return companies


@router.post("/", response_model=schemas.Company)
def create_company(
    *,
    db: Session = Depends(deps.get_db),
    company_in: schemas.CompanyCreate,
) -> Any:
    """
    Create new company.
    """
    company = crud.company.create(db=db, obj_in=company_in)
    return company


@router.put("/{id}", response_model=schemas.Company)
def update_company(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    company_in: schemas.CompanyUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a company.
    """
    company = crud.company.get(db=db, id=id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    company = crud.company.update(db=db, db_obj=company, obj_in=company_in)
    return company


@router.get("/{id}", response_model=schemas.Company)
def read_company(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get company by ID.
    """
    company = crud.company.get(db=db, id=id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{id}", response_model=schemas.Company)
def delete_company(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a company.
    """
    company = crud.company.get(db=db, id=id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    company = crud.company.remove(db=db, id=id)
    return company
