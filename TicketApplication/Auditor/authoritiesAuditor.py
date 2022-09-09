import urllib.request
from functools import wraps

import py_eureka_client.eureka_client as eureka_client
from flask_restful import abort


class AuthoritiesAuditor:
    @staticmethod
    def secured(permissions):
        def decorate(f):
            @wraps(f)
            def checker(*args, **kwargs):
                user_type = kwargs['jwt_decoded']['type']
                response = eureka_client.do_service('user-application-server',
                                                    f'/auth/hasAuthority?receivedUserType={user_type}&questionedPermission={permissions}')
                if response == 'true':
                    return f(*args, **kwargs)
                else:
                    return abort(401)

            return checker

        return decorate
