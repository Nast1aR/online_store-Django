from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
    
    def create_guest_user(self):
        guest_first_name = "guest_" + get_random_string(length=8)

        guest_user = self.model(first_name=guest_first_name)
        guest_user.save(using=self._db)
        return guest_user