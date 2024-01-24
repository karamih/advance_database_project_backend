from sqlalchemy import Column, Integer, Float, DECIMAL, Date, String, Time, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

from app.database import Base


class Branch(Base):
    __tablename__ = 'ET_BRANCH'

    A_branchNo = Column(String(6), primary_key=True, nullable=False)
    A_country = Column(String(10))
    A_state = Column(String(50))
    A_city = Column(String(50))
    A_street = Column(String(50))
    A_phoneNo = Column(String(11))
    A_score = Column(DECIMAL(precision=3, scale=2))
    A_openingTime = Column(Time)
    A_closingTime = Column(Time)
    A_startDate = Column(Date)


class PerchasingOfficer(Base):
    __tablename__ = 'ET_PERCHASINGOFFICER'

    A_employeeNo = Column(String(16), primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_firstName = Column(String(100))
    A_lastName = Column(String(50))
    A_age = Column(Integer)
    A_gender = Column(String(3))
    A_salary = Column(Integer)
    A_phoneNo = Column(String(11))

    owner = relationship("Branch")


class Manager(Base):
    __tablename__ = 'ET_MANAGER'

    A_employeeNo = Column(String(16), primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_firstName = Column(String(100))
    A_lastName = Column(String(50))
    A_age = Column(Integer)
    A_gender = Column(String(3))
    A_salary = Column(Integer)
    A_phoneNo = Column(String(11))

    owner = relationship("Branch")


class Barista(Base):
    __tablename__ = 'ET_BARISTA'

    A_employeeNo = Column(String(16), primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_firstName = Column(String(100))
    A_lastName = Column(String(50))
    A_age = Column(Integer)
    A_gender = Column(String(3))
    A_salary = Column(Integer)
    A_phoneNo = Column(String(11))

    owner = relationship("Branch")


class Menu(Base):
    __tablename__ = 'ET_MENU'

    A_itemID = Column(String(6), primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_itemName = Column(String(50))
    A_price = Column(Integer)
    A_recipe = Column(String(300))
    A_averageScore = Column(Float, nullable=False)

    owner = relationship("Branch")


class Equipment(Base):
    __tablename__ = 'ET_EQUIPMENT'

    A_equipmentNo = Column(String(15), primary_key=True, nullable=False)
    A_equipmentName = Column(String(100), nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_equipDate = Column(Date)
    A_equipmentValue = Column(Integer)
    A_equipmentStatus = Column(String(100))
    A_equipmentColor = Column(String(50))

    owner = relationship("Branch")


class MonthlyExpense(Base):
    __tablename__ = 'ET_MONTHLYEXPENSE'

    A_expenseID = Column(Integer, primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_year = Column(String(4))
    A_month = Column(String(20))
    A_rent = Column(Integer)
    A_totalSalary = Column(Integer)
    A_bill = Column(Integer)
    A_ingredient = Column(Integer)
    A_total = Column(Integer)

    owner = relationship("Branch")


class Customer(Base):
    __tablename__ = 'ET_CUSTOMER'

    A_customerID = Column(String(20), primary_key=True, nullable=False)
    A_firstName = Column(String(50))
    A_lastName = Column(String(50))
    A_age = Column(Integer)
    A_gender = Column(String(3))
    A_phoneNumber = Column(String(11))


class Complaint(Base):
    __tablename__ = 'RT_COMPLAINT'

    A_complaintID = Column(Integer, primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_customerID = Column(String(20), ForeignKey('ET_CUSTOMER.A_customerID'), nullable=False)
    A_content = Column(Text, nullable=False)
    A_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("Branch")
    owner = relationship("Customer")


class Cashier(Base):
    __tablename__ = 'ET_CASHIER'

    A_employeeNo = Column(String(16), primary_key=True, nullable=False)
    A_branchNo = Column(String(6), ForeignKey('ET_BRANCH.A_branchNo'), nullable=False)
    A_firstName = Column(String(50))
    A_lastName = Column(String(50))
    A_age = Column(Integer)
    A_gender = Column(String(3))
    A_salary = Column(DECIMAL(precision=10, scale=2))
    A_phoneNo = Column(String(11))
    A_password = Column(String(20), nullable=False)

    owner = relationship("Branch")


class Order(Base):
    __tablename__ = 'RT_ORDER'

    A_orderID = Column(Integer, primary_key=True, nullable=False)
    A_employeeNo = Column(String(16), ForeignKey('ET_CASHIER.A_employeeNo'), nullable=False)
    A_customerID = Column(String(20), ForeignKey('ET_CUSTOMER.A_customerID'), nullable=False)
    A_totalPrice = Column(DECIMAL(30, 2), nullable=False)
    A_created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("Cashier")
    owner = relationship("Customer")


class OrderdItem(Base):
    __tablename__ = 'ET_ORDEREDITEM'

    A_orderID = Column(Integer, ForeignKey('RT_ORDER.A_orderID'), primary_key=True, nullable=False)
    A_itemID = Column(String(6), ForeignKey('ET_MENU.A_itemID'), primary_key=True, nullable=False)
    A_itemScore = Column(Float, nullable=False)

    owner = relationship("Order")
    owner = relationship("Menu")
