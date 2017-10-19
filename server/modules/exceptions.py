class UserDoesNotExist(Exception):
    pass


class PasswordDoesNotMatch(Exception):
    pass


class RegistrationLinkExpired(Exception):
    pass


class UserAlreadyExist(Exception):
    pass
