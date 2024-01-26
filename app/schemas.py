from pydantic import BaseModel


class GetBranchOutput(BaseModel):
    A_city: str
    A_street: str
    A_phoneNo: str

    class config:
        orm_mode = True


class GetBranchMenuOutput(BaseModel):
    A_itemName: str
    A_itemName: str
    A_price: int
    A_averageScore: float

    class config:
        orm_mode = True

class GetEmployeeOutput(BaseModel):
    A_firstName: str
    A_lastName: str
    A_age: int
    A_gender: str
    A_phoneNo: str
    A_password: str

    class config:
        orm_mode = True