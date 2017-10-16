from .views import *

routes = [
    {'method': 'GET', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': '*', 'path': '/api/register', 'handler': RegistrationView,  'name': 'users'}
]
