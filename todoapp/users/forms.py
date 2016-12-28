from django.apps import apps
from django import forms
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        if "email" not in cleaned_data or "password" not in cleaned_data:
            return cleaned_data

        model_cls = apps.get_model("users.User")
        email = cleaned_data["email"]
        password = cleaned_data["password"]

        try:
            user = model_cls.objects.get(email=email)
            if user.check_password(password) and user.is_active:
                return cleaned_data
        except model_cls.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            model_cls().set_password(password)

        errormsg = _("Login failed, review your credentials and try again.")
        self.add_error("email", errormsg)
        self.add_error("password", errormsg)

        return cleaned_data
