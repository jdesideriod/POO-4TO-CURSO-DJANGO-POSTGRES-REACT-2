
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")

    def save(self, commit=True):
        user = super().save(commit=False)

        #  asegura contraseña encriptada
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user