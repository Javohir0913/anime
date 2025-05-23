from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .form import AnimeForm
from .models import AnimeTags, Anime, Episode


# Create your views here.
# ------------------------ Tag --------------------------
class AnimeTagsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AnimeTags
    template_name = 'tag/create.html'
    fields = ['tag_name']
    success_url = reverse_lazy('anime-tags-list')

    def test_func(self):
        return self.request.user.is_staff


class AnimeTagsEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AnimeTags
    template_name = 'tag/edit.html'
    fields = ['tag_name']
    success_url = reverse_lazy('anime-tags-list')

    def test_func(self):
        return self.request.user.is_staff


class AnimeTagsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = AnimeTags
    template_name = 'tag/list-view.html'
    context_object_name = 'tags'

    def test_func(self):
        return self.request.user.is_staff


class AnimeTagsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AnimeTags
    template_name = 'tag/delete.html'
    success_url = reverse_lazy('anime-tags-list')

    def test_func(self):
        return self.request.user.is_staff


# ----------------------- Anime -----------------------
class AnimeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'anime/create.html'
    success_url = reverse_lazy('anime-list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anime_tags'] = AnimeTags.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        print("Form is invalid")
        print(self.request.POST)
        print(form.errors)
        return super().form_invalid(form)


class AnimeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Anime
    template_name = 'anime/list-view.html'
    context_object_name = 'anime_all'

    def test_func(self):
        return self.request.user.is_staff


class AnimeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anime
    template_name = 'anime/edit.html'
    fields = ['name', 'image', 'anime_tags', 'year', 'age_rating', 'season', ]
    success_url = reverse_lazy('anime-list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anime_tags'] = AnimeTags.objects.all()
        return context


class AnimeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anime
    template_name = 'anime/delete.html'
    success_url = reverse_lazy('anime-list')

    def test_func(self):
        return self.request.user.is_staff


# ----------------------- Episode -----------------------
class EpisodeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Episode
    template_name = 'episode/create.html'
    fields = ['title', 'url_video', 'studio', 'quality', 'part', 'anime_info', ]
    success_url = reverse_lazy('episode-list')

    def test_func(self):
        return self.request.user.is_staff


class EpisodeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Episode
    template_name = 'episode/list-view.html'
    context_object_name = 'episodes'

    def test_func(self):
        return self.request.user.is_staff


class EpisodeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Episode
    template_name = 'episode/edit.html'
    fields = ['title', 'url_video', 'studio', 'quality', 'part', 'anime_info', ]
    success_url = reverse_lazy('episode-list')

    def test_func(self):
        return self.request.user.is_staff


class EpisodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Episode
    template_name = 'episode/delete.html'
    success_url = reverse_lazy('episode-list')

    def test_func(self):
        return self.request.user.is_staff

