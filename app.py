from flask import Flask, jsonify, request
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

    def post(self):
        data = request.json
        response = todos.create_task(data["id"], data["title"])
        return response

    def put(self):
        data = request.json
        if data["status"] not in ['CLOSED', 'OPEN']:
            return {'error':'status can only be "OPEN" or "CLOSED"'}, 400
        response = todos.update_task(data["id"], data["status"])
        return response

    def delete(self):
        data = request.json
        response = todos.delete_task(data["id"])
        return response

class Task(Resource):
    def get(self, task_id):
        task = todos.get_task(task_id)
        return {'task':task}

api.add_resource(Health, '/health/')
api.add_resource(Tasks, '/tasks/')
api.add_resource(Task, '/task/<str:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
