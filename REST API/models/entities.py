from db import db

class Employee(db.Model):
    __tablename__ = "Employee"

    id = db.Column(db.Integer, primary_key=True)
    checked = db.Column(db.Boolean, unique=False, default=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    type= db.Column(db.String(80), nullable=False, unique=True)
    age = db.Column(db.Numeric(10,2))
    description = db.Column(db.String(100), nullable=False, unique=True)
    




def __repr__(self):
    return 'EmployeeModel(id=%d, checked=%r,name=%s,type=%s,age=%f,description =%s)' % (self.id,self.checked,self.name, self.type,self.age,self.description)
    
def json(self):
    return {'id':self.id,'checked':self.checked,'name': self.name,'type': self.type,'age': self.age,'description': self.description}
        


    
    
    