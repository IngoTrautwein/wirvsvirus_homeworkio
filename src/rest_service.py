from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from server.homework_io_administration import HomeworkIOAdministration

app = Flask(__name__)

CORS(app, resources=r'/homeworkio/*')

api = Api(app, version='1.0', title='HomeworkIO API',
    description='Dies ist eine API.')

homeworkio = api.namespace('homeworkio', description='Funktionen der homeworkio')

bo = api.model('BusinessObject', {
    'id': fields.Integer(readonly=True, attribute='_id', description='Der Unique Identifier eines Business Object'),
})

student = api.inherit('Student', bo, {
    'first_name': fields.String(required=True, attribute='_first_name', description='Vorname Student'),
    'surname': fields.String(required=True, attribute='_surname', description='Nachname Student')
})

teacher = api.inherit('Teacher', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname Teacher'),
    'surname': fields.String(attribute='_surname', description='Nachname Teacher')
})

school = api.inherit('School', bo, {
    'name': fields.String(attribute='_name', description='Name der School')
})

school_class = api.inherit('SchoolClass', bo, {
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
        try:
            first_name = api.payload["first_name"]
            surname = api.payload["surname"]
            return adm.create_student(first_name, surname), 200
        except KeyError:
            return "KeyError", 500

@homeworkio.route('/students/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID des Studenten')
class StudentOperations(Resource):
    @homeworkio.marshal_with(student)
    def get(self, id):
        """Auslesen eines bestimmten Customer-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = HomeworkIOAdministration()
        student = adm.get_student_by_id(id)
        return student

    def delete(self, id):
        """Löschen eines bestimmten Customer-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = HomeworkIOAdministration()
        student = adm.get_student_by_id(id)
        adm.delete_student(student)
        return '', 200

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
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()
        try:
            first_name = api.payload["first_name"]
            surname = api.payload["surname"]
            return adm.create_teacher(first_name, surname), 200
        except KeyError:
            return "KeyError", 500

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
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()
        try:
            name = api.payload["name"]
            return adm.create_school_class(name), 200
        except KeyError:
            return "KeyError", 500

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
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()
        try:
            name = api.payload["name"]
            return adm.create_school(name), 200
        except KeyError:
            return "KeyError", 500


if __name__ == '__main__':
    app.run(debug=True)