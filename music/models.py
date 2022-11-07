from django.conf import settings
from django.db import models

# Create your models here.


class Term(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    images = models.JSONField(default=None, blank=True, null=True)
    audio_url = models.CharField(max_length=250, default=None, blank=True, null=True)
    video_url = models.CharField(max_length=250, default=None, blank=True, null=True)

    def get_annotation_locale_or_default(self, locales):
        for locale in locales:
            an_locale = Annotation.objects.get(parent_term=self.pk, locale=locale)
            if an_locale:
                return an_locale
        return Annotation.objects.get(parent_term=self.pk, locale=settings.DEFAULT_TERM_LOCALE)


class Annotation(models.Model):
    explanation = models.TextField()
    locale = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    parent_term = models.ForeignKey(Term, on_delete=models.CASCADE, default=None, blank=True, null=True)

