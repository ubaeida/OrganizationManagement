from functools import wraps

import jwt
from Auditor.authoritiesAuditor import AuthoritiesAuditor
from appSettings import request, app

authoritiesAuditor = AuthoritiesAuditor()


class JwtAspect:
    @staticmethod
    def jwt_secured(f):
        @wraps(f)
        def validate_jwt(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
            if not token:
                return {
                           "message": "Authentication Token is missing!",
                           "data": None,
                           "error": "Unauthorized"
                       }, 401
            try:
                data = jwt.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
                kwargs['jwt_decoded'] = data
            except Exception as e:
                return {
                           "message": "Something went wrong",
                           "data": None,
                           "error": str(e)
                       }, 500
            return f(*args, **kwargs)

        return validate_jwt
