import unittest
from app import app
from app.models import Todo

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        todos = Todo.objects.all()
        for todo in todos:
            todo.delete()

    def test_index(self):
        rv =self.app.get('/')
        assert "Todo" in rv.data

    def test_todo(self):
        self.app.post('/add', data = dict(content="test123"))
        todo = Todo.objects.get(content="test123")
        assert todo is not None

    def test_done(self):
        todos = Todo.objects.all()
        for todo in todos:
            if todo.status == 0:
                str = '/done/' + todo.id.__str__
                self.app.post(str)
                todo = Todo.objects.get(id=todo.id)
                assert todo.status == 1
            else:
                str = '/undone/' + todo.id.__str__
                self.app.post(str)
                todo = Todo.objects.get(id=todo.id)
                assert todo.status == 0