import inject

from app.ports import ITodoRepository


class TodoItemView(object):

    def __init__(self, repository: ITodoRepository, todo_id: str):
        self.repository = repository
        self.todo_id = todo_id

    def __call__(self):
        return self.repository.get(self.todo_id)


class TodoListView(object):

    def __init__(self, repository: ITodoRepository):
        self.repository = repository

    def __call__(self):
        return self.repository.get_all()


class TodoViewFactory(object):

    @inject.autoparams("repository")
    def __init__(self, repository: ITodoRepository):
        self.repository = repository

    def __call__(self, todo_id: str = None):
        view = TodoListView(self.repository) if todo_id is None else TodoItemView(self.repository, todo_id)
        return view()
