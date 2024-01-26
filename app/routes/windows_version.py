from typing import List
from fastapi import Depends, status, APIRouter, HTTPException

from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/windows", tags=["windows routes"])


@router.get('/login', status_code=status.HTTP_200_OK, response_model=schemas.GetEmployeeOutput)
def login(employeeNo: str, password: str, db: Session = Depends(get_db)):
    employee = db.query(models.Cashier).filter(models.Cashier.A_employeeNo == employeeNo, models.Cashier.A_password == password).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no employee.")
    return employee


@router.get('/addCustomer', status_code=status.HTTP_200_OK)
def addCustomer(id: str, firstName: str, lastName: str, phoneNumber: str, gender: str, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.A_customerID == id).first()
    if customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="valid customer.")

    customer_data = {
        "A_customerID": id,
        "A_firstName": firstName,
        "A_lastName": lastName,
        "A_gender": gender,
        "A_phoneNumber": phoneNumber
    }
    new_customer = models.Customer(**customer_data)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return "Done"