import json
from nameko.web.handlers import http


# TODO: dummy data
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


class HttpService:
    name = "http_service"

    @http('GET', '/todos/<string:todo_id>')
    def get_todo(self, request, todo_id):
        if todo_id in TODOS:
            return json.dumps(TODOS[todo_id])
        else:
            return json.dumps({'error': 'not found'})


    @http('GET', '/todos')
    def get_todos(self, request):
        return json.dumps(TODOS)
