from .views import UserView, BaseView

routes = [
    {'method': '*', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': '*', 'path': '/api/users', 'handler': UserView,  'name': 'users'}
]
