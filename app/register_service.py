
class RegisterService:
    """
    Handling user registration
    Args:
        payload: request body on /register route
    """
    def __init__(self,  payload=None):
        self.payload = payload
        self.users = {"users": []}
        self.key = 'user'

    def create(self):
        """
        Creates the user
        Returns:
            user dict
        """
        user = {
                    self.payload['user_name']: {
                            "first_name":self.payload['first_name'],
                            "email":self.payload['email'],
                            "pass":self.payload['password'],
                            "pass_confirm":self.payload['password_confirmation']
                    }
                }

        self.users['users'].append(user)

        return user

    def create_response(self):
        """
        Creating register response
        """
        obj = {}
        obj['name'] = self.payload['first_name']
        obj['user_name'] = self.payload['user_name']
        obj['email'] = self.payload['email']

        result = self._wrap_response(obj)

        return result

    def _wrap_response(self, obj):
        """
        Wrapping response into self.key value
        """
        result_with_wrapper = {}
        result_with_wrapper[self.key] = obj
        return result_with_wrapper

    def validate_user(self):
        """
        Validating reuqest body
        Returns:
            errors list in case request body not valid
        """
        errors = []
        if 'first_name' not in self.payload:
            errors.append('name is required field')
        if 'user_name' not in self.payload:
            errors.append('user_name is required field')
        if 'email' not in self.payload:
            errors.append('email is required field')
        if 'password' not in self.payload:
            errors.append('password is required field')
        if 'password_confirmation' not in self.payload:
            errors.append('password_confirmation is required field')

        return errors
