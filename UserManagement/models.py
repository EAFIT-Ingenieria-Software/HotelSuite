from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # id
    # first_name
    second_name = models.CharField(max_length=50, default="")
    # last_name
    # email
    # password
    role = models.CharField(max_length=10, default="customer")
    phone = models.CharField(max_length=10, default="0000000000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_second_name(self):
        return self.second_name

    def set_second_name(self, second_name):
        self.second_name = second_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at
