from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(
        max_length=5,
        required=True,
        validators=[RegexValidator(regex='^\d{5}$', message='Zip code must be exactly 5 digits.')]
    )
    phone_number = forms.CharField(
        max_length=10,
        required=True,
        validators=[RegexValidator(regex='^\d{10}$', message='Phone number must be exactly 10 digits.')]
    )

    class Meta:
        model = CustomUser
        fields = ("username", "name", "email", "password1", "password2", 'address', 'city', 'zip_code', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Add 'form-control' class for Bootstrap

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
