from django.urls import path

from homepage_app.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),  # Home page URL
]