from .views import (
    BaseView, RegistrationView, LoginView, ProfileView
)

routes = [
    {'method': '*', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': '*', 'path': '/api/register', 'handler': RegistrationView,  'name': 'users'},
    {'method': '*', 'path': '/api/login', 'handler': LoginView,  'name': 'login'},
    {'method': '*', 'path': '/api/profile', 'handler': ProfileView,  'name': 'profile'}
]
