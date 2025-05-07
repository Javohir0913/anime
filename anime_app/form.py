from django import forms

from anime_app.models import AnimeTags, Anime


class AnimeForm(forms.ModelForm):
    anime_tags = forms.ModelMultipleChoiceField(
        queryset=AnimeTags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Anime
        fields = ['name', 'image', 'year', 'age_rating', 'season', 'anime_tags']