class Role:
    ADMIN = 'AD'
    USER = 'USR'

    @classmethod
    def choices(cls):
        return (
            (cls.ADMIN, 'Admin'),
            (cls.USER, 'User'),
        )
