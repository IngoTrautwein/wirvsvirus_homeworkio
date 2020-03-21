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
    'name': fields.String(attribute='_name', description='Name der School')
})

school_class = homeworkio.inherit('SchoolClass', bo, {
    'name': fields.String(attribute='_name', description='Name der School_Class')
})

@homeworkio.route('/helloworld')
@homeworkio.response(200, 'Alles ok.')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200

@homeworkio.route('/students')
@homeworkio.response(500, 'Serverseitiger Fehler')
class StudentListOperations(Resource):
    @homeworkio.marshal_list_with(student)
    def get(self):
        adm = HomeworkIOAdministration()
        students = adm.get_all_students()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return students

    @homeworkio.marshal_with(student, code=200)
    @homeworkio.expect(student)
    def post(self):
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()

        return "not implemented yet", 200

@homeworkio.route('/teachers')
@homeworkio.response(500, 'Serverseitiger Fehler')
class TeacherListOperations(Resource):
    @homeworkio.marshal_list_with(teacher)
    def get(self):
        adm = HomeworkIOAdministration()
        teachers = adm.get_all_teachers()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return teachers

    @homeworkio.marshal_with(teacher, code=200)
    @homeworkio.expect(teacher)
    def post(self):
        """Anlegen eines neuen Teachers."""
        adm = HomeworkIOAdministration()

        return "not implemented yet", 200

@homeworkio.route('/school_classes')
@homeworkio.response(500, 'Serverseitiger Fehler')
class School_ClassListOperations(Resource):
    @homeworkio.marshal_list_with(school_class)
    def get(self):
        adm = HomeworkIOAdministration()
        school_classes = adm.get_all_school_classes()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return school_classes

    @homeworkio.marshal_with(school_class, code=200)
    @homeworkio.expect(school_class)
    def post(self):
        """Anlegen eines neuen school_class."""
        adm = HomeworkIOAdministration()

        return "not implemented yet", 200

@homeworkio.route('/schools')
@homeworkio.response(500, 'Serverseitiger Fehler')
class SchoolListOperations(Resource):
    @homeworkio.marshal_list_with(school)
    def get(self):
        adm = HomeworkIOAdministration()
        schools = adm.get_all_schools()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return schools

    @homeworkio.marshal_with(school, code=200)
    @homeworkio.expect(school)
    def post(self):
        """Anlegen eines neuen school."""
        adm = HomeworkIOAdministration()

        return "not implemented yet", 200


if __name__ == '__main__':
    app.run(debug=True)