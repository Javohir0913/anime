from django.contrib import admin

from .models import AnimeTags, Anime, Episode, WeekAnime


# Register your models here.
class WeekAnimeAdmin(admin.ModelAdmin):
    list_filter = ('day',)


admin.site.register(AnimeTags)
admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(WeekAnime, WeekAnimeAdmin)