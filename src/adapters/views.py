import inject

from adapters.presenters import IPresenter, NoOpPresenter
from app.ports import ITodoRepository


class TodoView(object):

    @inject.autoparams("repository")
    def __init__(self, repository: ITodoRepository,  presenter: IPresenter = None):
        self.presenter = NoOpPresenter() if presenter is None else presenter
        self.repository = repository


class TodoItemView(TodoView):

    def __call__(self, todo_id):
        return self.presenter(self.repository.get(todo_id))


class TodoListView(TodoView):

    def __call__(self):
        return [self.presenter(t) for t in self.repository.get_all()]
