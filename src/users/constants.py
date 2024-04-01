class Role:
    ADMIN = 'admin'
    USER = 'user'
    GUEST = "Guest"


    @classmethod
    def choices(cls):
        return (
            (cls.ADMIN, 'Admin'),
            (cls.USER, 'User'),
            (cls.GUEST, 'Guest'),
        )
