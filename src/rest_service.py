import os

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from werkzeug.utils import secure_filename

from server.homework_io_administration import HomeworkIOAdministration
from definitions import UPLOAD_FOLDER_PATH

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH

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

subject = api.inherit('Subject', bo, {
    'name': fields.String(attribute='_name', description='Name des Subjects')
})

homework = api.inherit('Homework', bo, {
    'name': fields.String(attribute='_name', description='Name der Hausaufgabe'),
    'file_path': fields.String(attribute='_file_path', description='Dateipfad der Hausaufgabe'),
    'description': fields.String(attribute='_description', description='Beschreibung der Hausaufgabe'),
    'start_event': fields.DateTime(attribute='_start_event', description='Start_Event der Hausaufgabe'),
    'end_event': fields.DateTime(attribute='_end_event', description='End_Event der Hausaufgabe'),
    'sub_school_id': fields.Integer(attribute='_name', description='subject_id der Hausaufgabe')
})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@homeworkio.route('/file-upload')
@homeworkio.response(200, 'Alles ok.')
class FileUpload(Resource):

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp

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
        adm = HomeworkIOAdministration()
        student = adm.get_student_by_id(id)
        return student

    def delete(self, id):
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

@homeworkio.route('/teachers/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID des Teachers')
class TeacherOperations(Resource):
    @homeworkio.marshal_with(teacher)
    def get(self, id):
        adm = HomeworkIOAdministration()
        teacher = adm.get_teacher_by_id(id)
        return teacher

    def delete(self, id):
        adm = HomeworkIOAdministration()
        teacher = adm.get_teacher_by_id(id)
        adm.delete_teacher(teacher)
        return '', 200

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

@homeworkio.route('/school_classes/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID der school_classes')
class School_ClassOperations(Resource):
    @homeworkio.marshal_with(school_class)
    def get(self, id):
        adm = HomeworkIOAdministration()
        school_class = adm.get_school_class_by_id(id)
        return school_class

    def delete(self, id):
        adm = HomeworkIOAdministration()
        school_class = adm.get_school_class_by_id(id)
        adm.delete_school_class(school_class)
        return '', 200

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
            address = api.payload["address"]
            return adm.create_school(name, address), 200
        except KeyError:
            return "KeyError", 500

@homeworkio.route('/schools/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID der schools')
class SchoolOperations(Resource):
    @homeworkio.marshal_with(school)
    def get(self, id):
        adm = HomeworkIOAdministration()
        school = adm.get_school_by_id(id)
        return school

    def delete(self, id):
        adm = HomeworkIOAdministration()
        school = adm.get_school_by_id(id)
        adm.delete_school(school)
        return '', 200

@homeworkio.route('/subjects')
@homeworkio.response(500, 'Serverseitiger Fehler')
class SubjectListOperations(Resource):
    @homeworkio.marshal_list_with(subject)
    def get(self):
        adm = HomeworkIOAdministration()
        subjects = adm.get_all_subjects()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return subjects

    @homeworkio.marshal_with(subject, code=200)
    @homeworkio.expect(subject)
    def post(self):
        """Anlegen eines neuen Studenten."""
        adm = HomeworkIOAdministration()
        try:
            name = api.payload["name"]
            return adm.create_subject(name), 200
        except KeyError:
            return "KeyError", 500

@homeworkio.route('/subjects/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID der subjects')
class SubjectOperations(Resource):
    @homeworkio.marshal_with(subject)
    def get(self, id):
        adm = HomeworkIOAdministration()
        school = adm.get_subject_by_id(id)
        return school

    def delete(self, id):
        adm = HomeworkIOAdministration()
        subject = adm.get_subject_by_id(id)
        adm.delete_subject(subject)
        return '', 200

@homeworkio.route('/homeworks')
@homeworkio.response(500, 'Serverseitiger Fehler')
class HomeworkListOperations(Resource):
    @homeworkio.marshal_list_with(homework)
    def get(self):
        adm = HomeworkIOAdministration()
        homeworks = adm.get_all_homeworks()
        # Wenn leer, wird eine leere Liste zurückgegeben
        return homeworks

    @homeworkio.marshal_with(homework, code=200)
    @homeworkio.expect(homework)
    def post(self):
        adm = HomeworkIOAdministration()
        try:
            description = api.payload["description"]
            file_path = api.payload["file_path"]
            start_event = api.payload["start_event"]
            end_event = api.payload["end_event"]
            subject_id = api.payload["subject_id"]
            school_class_id = api.payload["school_class_id"]
            return adm.create_homework(description, file_path, start_event, end_event, school_class_id, subject_id), 200
        except KeyError:
            return "KeyError", 500

@homeworkio.route('/homeworks/<int:id>')
@homeworkio.response(500, 'Server Fehler.')
@homeworkio.param('id', 'ID der Homework')
class HomeworkOperations(Resource):
    @homeworkio.marshal_with(subject)
    def get(self, id):
        adm = HomeworkIOAdministration()
        homework = adm.get_homework_by_id(id)
        return homework

    def delete(self, id):
        adm = HomeworkIOAdministration()
        homework = adm.get_homework_by_id(id)
        adm.delete_homework(homework)
        return '', 200


if __name__ == '__main__':
    app.run(debug=True)
