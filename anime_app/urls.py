from django.urls import path

from .views import (
    AnimeTagsCreateView,
    AnimeTagsListView,
    AnimeTagsEditView,
    AnimeTagsDeleteView,
    AnimeCreateView,
    AnimeListView,
)

urlpatterns = [
    # ------------------------ Tag ---------------------------
    path('creat-tag/', AnimeTagsCreateView.as_view(), name='anime-tags-create'),
    path('list-tag/', AnimeTagsListView.as_view(), name='anime-tags-list'),
    path('edit-tag/<int:pk>/', AnimeTagsEditView.as_view(), name='anime-tags-edit'),
    path('delete-tag/<int:pk>/', AnimeTagsDeleteView.as_view(), name='anime-tags-delete'),

    # --------------------------- Anime -------------------------------------
    path('anime-create/', AnimeCreateView.as_view(), name='anime-create'),
    path('anime-list/', AnimeListView.as_view(), name='anime-list'),
]
