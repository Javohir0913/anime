from django.urls import path

from .views import logout_view, signup_and_login, check_username

urlpatterns = [
    path('login-and-register/', signup_and_login, name='login-register'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check-username'),
]