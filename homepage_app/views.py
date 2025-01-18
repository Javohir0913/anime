import requests
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        print(ip)
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print({
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country")
        })
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = User.objects.get(pk=self.request.user.pk)
        context['info'] = {
            "ip": data.get('ip'),
            "city": data.get('city'),
            "region": data.get('region'),
            "country": data.get('country')
        }
        return context
    