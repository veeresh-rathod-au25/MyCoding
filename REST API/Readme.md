**Sample Flask application using OpenAPI ,Connexion, Flask-Marshmallow and Flask-SQLAlchemy**

**OpenAPI**
OpenAPI Specification (formerly Swagger Specification) is an API description format for REST APIs. API specifications can be written in YAML or JSON. The format is easy to learn and readable to both humans and machines. The complete OpenAPI Specification can be found on GitHub: OpenAPI 3.0 Specification

**Connexion**
Connexion is a framework that automagically handles HTTP requests based on OpenAPI Specification (formerly known as Swagger Spec) of your API described in YAML format. Connexion allows to write an OpenAPI specification, then maps the endpoints to Python functions; this makes it unique, as many tools generate the specification based on Python code.

**Setting up the VirtualEnv and install dependencies**
Go inside the project folder and execute the below commands. We will use Pipenv to setup the VirtualEnv.

pipenv shell
pipenv install

**Run the Application**
python app.py

**This will start the application on port 5000**

**Test the application**

![image](https://user-images.githubusercontent.com/85392456/161424366-523247ed-6d3d-4772-aec6-b51e387bc4cb.png)


The server will start at http://localhost:5000/ui.

**Dependencies:**
flask, flask-marshmallow, flask-sqlalchemy, marshmallow-sqlalchemy and "connexion[swagger-ui]"

**entities.py** 
* Creating the Employee Model class
* Declared the table name employee where this model will be mapped to 
* we defined the table columns along with their data types
* Added some helper methods to print the object at runtime

**repositories.py**
* Creating the EmployeeRepo class
* Defined some helper methods, which we can use to perform CRUD operations on Employee entity.

**schemas.py** - need to create the schema for the Item Model class

**swagger.yml** - API specifications can be written in YAML or JSON format

**employee.py** - Contains all the functions with arguments specified in swagger.yml file. For example, def get(id) function

**app.py** - Starting Point

**data.db** - DB File
