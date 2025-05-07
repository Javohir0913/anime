from django.urls import path

from homepage_app.views import HomePageView, AnimeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),  # Home page URL
    # urls.py
    path('anime/view/<int:id>-<slug:name>/', AnimeView.as_view(), name='anime_view'),

]