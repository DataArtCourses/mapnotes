from .views import (
    BaseView, RegistrationView, LoginView, ProfileView, PinsView
)

routes = [
    {'method': '*', 'path': '', 'handler': BaseView, 'name': 'index'},
    {'method': '*', 'path': '/api/register', 'handler': RegistrationView,  'name': 'users'},
    {'method': '*', 'path': '/api/login', 'handler': LoginView,  'name': 'login'},
    {'method': '*', 'path': '/api/profile', 'handler': ProfileView,  'name': 'profile'},
    {'method': '*', 'path': '/api/pins', 'handler': PinsView, 'name': 'pins'}
]
