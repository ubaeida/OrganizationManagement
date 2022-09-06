import urllib.request
from functools import wraps

import py_eureka_client.eureka_client as eureka_client


class AuthoritiesAuditor:
    @staticmethod
    def secured(permission):
        def decorate(f):
            @wraps(f)
            def checker(*args, **kwargs):
                user_type = kwargs['jwt_decoded']['type']
                response = eureka_client.do_service('user-application-server',
                                                    f'/auth/hasAuthority?receivedUserType={user_type}&questionedPermission={permission}')
                if response == 'true':
                    return f(*args, **kwargs)
                else:
                    return {'message': 'user not allowed for this process'}

            return checker

        return decorate
