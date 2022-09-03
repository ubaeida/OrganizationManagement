class AuthoritiesAuditor:
    def links_access_auditor(self, user_type):
        print(user_type)
        if user_type == 'ADMINISTRATOR':
            return 'ADMINISTRATOR is connected to ticket application'
        return "couldn't find the user type"
