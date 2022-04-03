from db import db
from models.entities import Employee
from typing import List


class EmployeeRepo:
    
 def create(self,employee):
    db.session.add(employee)
    db.session.commit()
    
 def fetchById(self,_id)-> 'Employee':
     return db.session.query(Employee).filter_by(id=_id).first()
 
 def fetchAll(self) -> List['Employee']:
     return db.session.query(Employee).all()
 
 def delete(self,_id) -> None:
     employee= db.session.query(Employee).filter_by(id=_id).first()
     db.session.delete(employee)
     db.session.commit()
     
 def update(self,employee_data):
    db.session.merge(employee_data)
    db.session.commit()
    