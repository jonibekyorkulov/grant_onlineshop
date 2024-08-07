from django.urls import path
from apps.accounts.views import TestView, LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('', TestView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]