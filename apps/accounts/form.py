from django import forms
from apps.accounts.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be entered in the format: '+998XXXXXXXXX'. Up to 12 digits allowed."
)

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )
    phone = forms.CharField(validators=[phone_regex], max_length=13)

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError("Parollar bir biriga mos emas")
        return cleaned_data

    class Meta:
        model = User
        fields = ['phone', ]

