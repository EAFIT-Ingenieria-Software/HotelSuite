from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp, name="signup"),
    path("logout/", views.log_out, name="logout"),
]
