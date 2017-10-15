from .views import UserView, BaseView

routes = [
    {'method': 'GET', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': 'POST', 'path': '/api/users', 'handler': UserView,  'name': 'users'}
]
