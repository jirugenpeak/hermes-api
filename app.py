from flask import Flask, jsonify
from flask_restful import Api, Resource

import todos

app = Flask(__name__)
api = Api(app)

class Health(Resource):
    def get(self):
        return {'status':'ok'}, 200

class Tasks(Resource):
    def get(self):
        tasks = todos.get_tasks()
        return {'tasks':tasks}

    def post(self, id, title):
        response = todos.create_task(id, title)
        return response

    def update(self, id, status):
        if status not in ['CLOSED', 'OPEN']:
            return {'error':'status can only be "OPEN" or "CLOSED"'}, 400
        response = todos.update_task(id, status)
        return response

    def delete(self, id):
        response = todos.delete_task(id)
        return response
    

api.add_resource(Health, '/health/')
api.add_resource(Tasks, '/tasks/')

if __name__ == '__main__':
    app.run(debug=True)
