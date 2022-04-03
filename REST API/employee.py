from models.repositories import EmployeeRepo
from schemas.schemas import EmployeeSchema
from flask import request
from db import db

employeeRepo = EmployeeRepo()
employeeSchema = EmployeeSchema()
employeeListSchema = EmployeeSchema(many=True)
EMPLOYEE_NOT_FOUND = "Employee not found for id: {}"


def get(id):
    employee_data = employeeRepo.fetchById(id)
    if employee_data:
        return employeeSchema.dump(employee_data)
    return {'message': EMPLOYEE_NOT_FOUND.format(id)}, 404

def update(id):
    employee_data = employeeRepo.fetchById(id)
    employee_req_json = request.get_json()
    if employee_data:
        employee_data.checked = employee_req_json['checked']
        employee_data.name = employee_req_json['name']
        employee_data.type = employee_req_json['type']
        employee_data.age = employee_req_json['age']
        employee_data.description = employee_req_json['description']
        employeeRepo.update(employee_data)
        return employeeSchema.dump(employee_data)
    return {'message': EMPLOYEE_NOT_FOUND.format(id)}, 404

def delete(id):
    employee_data = employeeRepo.fetchById(id)
    if employee_data:
        employeeRepo.delete(id)
        return {'message': 'employee deleted successfully'}, 200
    return {'message': EMPLOYEE_NOT_FOUND.format(id)}, 404

def create():
    """print("e11111111111111111")"""
    employee_req_json = request.get_json()
    """print("emppppppppppppppppppppppppp",employee_req_json)"""
    employee_data = employeeSchema.load(employee_req_json,session=db.session)
    """print(employee_data)"""
    employeeRepo.create(employee_data)
    return employeeSchema.dump(employee_data),201

def getAll():
    return employeeListSchema.dump(employeeRepo.fetchAll()), 200
    