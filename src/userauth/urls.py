from django.urls import path 
from userauth import views

app_name= "userauth"

urlpatterns = [
    path("sign-up/", views.registration_view, name="sign-up")
]