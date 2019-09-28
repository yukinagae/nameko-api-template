import json
from nameko.web.handlers import http
from sqlalchemy import create_engine


# TODO: dummy data
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

# TODO: or fetch from database
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/todo')


class HttpService:
    name = "http_service"

    @http('GET', '/todos/<string:todo_id>')
    def get_todo(self, request, todo_id):
        with engine.connect() as con:
            result = con.execute('SELECT * FROM todo WHERE id = :id', {'id': todo_id})
            return json.dumps({'result': [dict(row) for row in result]})
        return json.dumps({'error': 'not found'})


    @http('GET', '/todos')
    def get_todos(self, request):
        with engine.connect() as con:
            result = con.execute('SELECT * FROM todo')
            return json.dumps({'result': [dict(row) for row in result]})
        return json.dumps({'error': 'not found'})
