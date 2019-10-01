from adapters.config import todo_read_repository
from adapters.presenters import IPresenter, NoOpPresenter


class TodoListView(object):

    def __init__(self, presenter: IPresenter = None):
        self.presenter = NoOpPresenter() if presenter is None else presenter

    def __call__(self):
        return [self.presenter(t) for t in todo_read_repository.get_all()]
