from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True


class AnimeTags(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name_plural = 'Anime Tags'
        verbose_name = 'Anime Tag'
        ordering = ['tag_name']
        unique_together = (('tag_name',),)


class Anime(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='anime_images')
    anime_tags = models.ManyToManyField(AnimeTags, blank=True, related_name='anime_tags')
    year = models.PositiveSmallIntegerField()
    age_rating = models.PositiveSmallIntegerField()
    season = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.year} {self.anime_tags}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        unique_together = (('name', 'year'),)


class Episode(BaseModel):
    class RoleChoice(models.TextChoices):
        quality_240 = '240', '240'
        quality_360 = '360', '360'
        quality_480 = '480', '480'
        quality_720 = '720', '720'
        quality_1080 = '1080', '1080'

    title = models.CharField(max_length=255)
    url_video = models.URLField()
    studio = models.CharField(max_length=255, blank=True, null=True)
    quality = models.CharField(max_length=100, choices=RoleChoice.choices, default=RoleChoice.quality_240)
    part = models.IntegerField()
    anime_info = models.ForeignKey('Anime', related_name='episodes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.part} {self.title} {self.quality}"

    class Meta:
        ordering = ['title']
        verbose_name = 'anime'
        verbose_name_plural = 'Episodes'
        unique_together = (('title', 'url_video'),)
