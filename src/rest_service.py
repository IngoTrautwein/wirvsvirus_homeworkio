from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources=r'/homeworkio/*')

homeworkio = Api(app, version='1.0', title='HomeworkIO API',
    description='Dies ist eine API.')

@homeworkio.route('/helloworld')
@homeworkio.response(200, 'Alles ok.')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200

if __name__ == '__main__':
    app.run(debug=True)