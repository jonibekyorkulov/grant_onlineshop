from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

class CustomPasswordResetForm(PasswordResetForm):
    phone = forms.CharField(max_length=50)

    def get_users(self, phone):
        active_users = User._default_manager.filter(phone__iexact=phone, is_active=True)
        return active_users

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        phone = self.cleaned_data["phone"]
        users = self.get_users(phone)
        if users:
            for user in users:
                # Send password reset notification to user's email, phone, etc.
                pass
