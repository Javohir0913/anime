from django.urls import path

from .views import logout_view, signup_and_login, check_username, UserProfileView, UserUpdateView

urlpatterns = [
    path('login-and-register/', signup_and_login, name='login-register'),
    path('logout/', logout_view, name='logout'),
    path('check-username/', check_username, name='check-username'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserUpdateView.as_view(), name='profile-edit'),
]