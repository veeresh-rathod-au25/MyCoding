from flask_marshmallow import Marshmallow
ma = Marshmallow()
from models.entities import Employee


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True