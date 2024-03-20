class User:
    def __init__(self, id, organizationId=None, email=None, username=None, full_name=None, sso_only=None, userRole=None, enabled=None, teamUsers=None, email_verified=None, tokens=None):
        self.id = id
        self.organizationId = organizationId
        self.email = email
        self.username = username
        self.full_name = full_name
        self.sso_only = sso_only
        self.userRole = userRole
        self.enabled = enabled
        self.teamUsers = teamUsers if teamUsers is not None else []
        self.email_verified = email_verified
        self.tokens = tokens if tokens is not None else []
