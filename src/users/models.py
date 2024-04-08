from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager
from django.conf import settings
from .constants import Role
from store.models import ProductInventory


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # password = models.CharField(max_length=100)
    favorite_products = models.ManyToManyField(ProductInventory,                              
               related_name='favorited_by', blank=True)
    image = models.ImageField(upload_to="uploads/images/users",blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20,choices=Role.choices(), default=Role.USER)
 
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email
        
    
# class UserImage(models.Model):
#     user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
#     filename = models.CharField(('filename'), max_length=255)

#     def __str__(self):
#         return self.filename
    
#изменила ипорт на модель ProductType   
class FavoriteProductInventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_favorite_products')
    product = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, related_name='favorited_products')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Date added")
    

    class Meta:
        unique_together = ['user', 'product']
        verbose_name = "Favorite Product"

