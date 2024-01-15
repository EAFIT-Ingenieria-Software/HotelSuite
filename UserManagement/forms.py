from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):
    second_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = (
            "first_name",
            "second_name",
            "last_name",
            "email",
            "phone",
            "password1",
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in [
            "first_name",
            "second_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2",
        ]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {"class": "form-control"})


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Email"
        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {"class": "form-control"})
