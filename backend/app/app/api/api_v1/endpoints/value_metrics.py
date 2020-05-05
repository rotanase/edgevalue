from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ValueMetric])
def read_value_metrics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve value metrics.
    """
    value_metrics = crud.value_metric.get_multi(db, skip=skip, limit=limit)
    return value_metrics


@router.post("/", response_model=schemas.ValueMetric)
def create_value_metric(
    *,
    db: Session = Depends(deps.get_db),
    value_metric_in: schemas.ValueMetricCreate,
) -> Any:
    """
    Create new value metric.
    """
    value_metric = crud.value_metric.create(db=db, obj_in=value_metric_in)
    return value_metric


@router.put("/{id}", response_model=schemas.ValueMetric)
def update_value_metric(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    value_metric_in: schemas.ValueMetricUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a value metric.
    """
    value_metric = crud.value_metric.get(db=db, id=id)
    if not value_metric:
        raise HTTPException(status_code=404, detail="Value metric not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    value_metric = crud.value_metric.update(db=db, db_obj=value_metric, obj_in=value_metric_in)
    return value_metric


@router.get("/{id}", response_model=schemas.ValueMetric)
def read_value_metric(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get value metric by ID.
    """
    value_metric = crud.value_metric.get(db=db, id=id)
    if not value_metric:
        raise HTTPException(status_code=404, detail="Value metric not found")
    return value_metric


@router.delete("/{id}", response_model=schemas.ValueMetric)
def delete_value_metric(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a value metric.
    """
    value_metric = crud.value_metric.get(db=db, id=id)
    if not value_metric:
        raise HTTPException(status_code=404, detail="Value metric not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    value_metric = crud.value_metric.remove(db=db, id=id)
    return value_metric
