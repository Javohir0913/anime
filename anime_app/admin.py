from django.contrib import admin

from .models import AnimeTags, Anime, Episode


# Register your models here.
admin.site.register(AnimeTags)
admin.site.register(Anime)
admin.site.register(Episode)