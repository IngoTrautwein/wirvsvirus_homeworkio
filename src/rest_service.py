from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from server.homework_io_administration import HomeworkIOAdministration

app = Flask(__name__)

CORS(app, resources=r'/homeworkio/*')

homeworkio = Api(app, version='1.0', title='HomeworkIO API',
    description='Dies ist eine API.')

bo = homeworkio.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
})

student = homeworkio.inherit('Student', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname Student'),
    'surname': fields.String(attribute='_surname', description='Nachname Student')
})

teacher = homeworkio.inherit('Teacher', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname Teacher'),
    'surname': fields.String(attribute='_surname', description='Nachname Teacher')
})

school = homeworkio.inherit('School', bo, {
    'name': fields.Integer(attribute='_name', description='Name der School')
})

school_class = homeworkio.inherit('SchoolClass', bo, {
    'name': fields.Integer(attribute='_name', description='Name der School_Class')
})

@homeworkio.route('/helloworld')
@homeworkio.response(200, 'Alles ok.')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200

@homeworkio.route('/students')
@homeworkio.response(500, 'Serverseitiger Fehler')
class CustomerListOperations(Resource):
    @homeworkio.marshal_list_with(student)
    def get(self):
        adm = HomeworkIOAdministration()
        students = adm.get_all_customers()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return students

    @homeworkio.marshal_with(student, code=200)
    @homeworkio.expect(student)
    def post(self):
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()

        return "not implemented yet", 200


if __name__ == '__main__':
    app.run(debug=True)