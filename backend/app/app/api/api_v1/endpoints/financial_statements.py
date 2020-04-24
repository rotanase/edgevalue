from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.FinancialStatement])
def read_financial_statements(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve financial statements.
    """
    financial_statements = crud.financial_statement.get_multi(db, skip=skip, limit=limit)
    return financial_statements


@router.post("/", response_model=schemas.FinancialStatement)
def create_financial_statement(
    *,
    db: Session = Depends(deps.get_db),
    financial_statement_in: schemas.FinancialStatementCreate,
) -> Any:
    """
    Create new financial statement.
    """
    financial_statement = crud.financial_statement.create(db=db, obj_in=financial_statement_in)
    return financial_statement


@router.put("/{id}", response_model=schemas.FinancialStatement)
def update_financial_statement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    financial_statement_in: schemas.FinancialStatementUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a financial statement.
    """
    financial_statement = crud.financial_statement.get(db=db, id=id)
    if not financial_statement:
        raise HTTPException(status_code=404, detail="Financial statement not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    financial_statement = crud.financial_statement.update(db=db, db_obj=financial_statement, obj_in=financial_statement_in)
    return financial_statement


@router.get("/{id}", response_model=schemas.FinancialStatement)
def read_financial_statement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get financial statement by ID.
    """
    financial_statement = crud.financial_statement.get(db=db, id=id)
    if not financial_statement:
        raise HTTPException(status_code=404, detail="Financial statement not found")
    return financial_statement


@router.delete("/{id}", response_model=schemas.FinancialStatement)
def delete_financial_statement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a financial statement.
    """
    financial_statement = crud.financial_statement.get(db=db, id=id)
    if not financial_statement:
        raise HTTPException(status_code=404, detail="Financial statement not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    financial_statement = crud.financial_statement.remove(db=db, id=id)
    return financial_statement
