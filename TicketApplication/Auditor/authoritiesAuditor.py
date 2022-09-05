from functools import wraps

import requests


class AuthoritiesAuditor:
    @staticmethod
    def secured(permission):
        def decorate(f):
            @wraps(f)
            def checker(*args, **kwargs):
                user_type = kwargs['jwt_decoded']['type']
                response = requests.get(
                    f'http://localhost:8060/auth/hasAuthority?receivedUserType={user_type}&questionedPermission={permission}')
                if response.content.decode('utf-8') == 'true':
                    print('User allowed')
                else:
                    print('user not allowed')
                return f(*args, **kwargs)

            return checker

        return decorate
