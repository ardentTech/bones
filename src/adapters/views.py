from adapters.config import todo_read_repository


class TodoListView(object):

    def __call__(self):
        return todo_read_repository.get_all()
