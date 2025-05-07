import requests
from datetime import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

from anime_app.models import Episode, WeekAnime
from django.core.paginator import Paginator


from homepage_app.helper import get_device_info
# Create your views here.

User = get_user_model()

class AnimeView(TemplateView):
    template_name = 'anime_view.html'

    def get_context_data(self, **kwargs):
        episodes = Episode.objects.filter(anime_info=self.kwargs['id']).order_by('part')
        context = {
            'episode_list': episodes,
        }
        return context
class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        # Bugungi sana
        today = datetime.today()
        day_of_week = today.strftime('%A').lower()

        # get() o‘rniga filter()
        week_animes = WeekAnime.objects.filter(day=day_of_week)

        episodes = Episode.objects.all().order_by('-created_at')[:10]

        paginator = Paginator(episodes, 2)  # Har bir sahifada 2 ta element

        page_number = self.request.GET.get('page')  # URL'dan page raqamini olish
        page_obj = paginator.get_page(page_number)  # Sahifani olish

        context = {
            'page_obj': page_obj,
            'week_animes': week_animes,  # Bu endi queryset bo‘ladi, list sifatida ishlatiladi
        }
        return context
