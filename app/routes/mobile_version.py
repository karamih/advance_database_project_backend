from typing import List
from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/mobile", tags=["mobile routes"])


@router.get('/branches', status_code=status.HTTP_200_OK, response_model=List[schemas.GetBranchOutput])
def get_branches(country: str, state: str, db: Session = Depends(get_db)):
    branches = db.query(models.Branch).filter(models.Branch.A_country == country, models.Branch.A_state == state).all()
    if not branches:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no cafe in {country}-{state}")
    return branches


@router.get('/branches-menu', status_code=status.HTTP_200_OK, response_model=List[schemas.GetBranchMenuOutput])
def get_branches_menu(branch_number: str, db: Session = Depends(get_db)):
    menu = db.query(models.Menu).filter(models.Menu.A_branchNo == branch_number).all()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid branch.")
    return menu
