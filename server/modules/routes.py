from .views import UserView, BaseView

routes = [
    ('GET', '', BaseView, 'index'),
    ('POST', '/api/users', UserView,  'users')
]
