from .views import UserView, BaseView

routes = [
    ('*', '', BaseView, 'index'),
    ('*', '/api/users', UserView,  'users')
]
