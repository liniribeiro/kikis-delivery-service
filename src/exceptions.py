class KikiError(Exception):
    name = None
    message = None
    error = None

    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.error = kwargs.get("error")
        self.name = kwargs.get("name")
        self.message = kwargs.get("message")

    def to_dict(self):
        return {
            'errors': {
                'name': self.name,
                'message': self.message,
                'error': self.error,
            }}


class AuthenticationError(KikiError):

    def to_dict(self):
        self.name = 'not-authorized'
        return {
            'errors': {
                'name': self.name
            }}


class PayloadError(KikiError):

    def to_dict(self):
        self.name = 'kiki-payload-error'
        self.message = 'O payload de input incorreto!'
        return {
            'errors': {
                'name': self.name,
                'message': self.message,
                'error': self.error,
            }}
