from .views import *

routes = [
    {'method': '*', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': '*', 'path': '/api/register', 'handler': RegistrationView,  'name': 'users'},
    {'method': '*', 'path': '/api/login', 'handler': LoginView,  'name': 'login'}
]
