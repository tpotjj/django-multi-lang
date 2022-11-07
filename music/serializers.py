from rest_framework import serializers
from .models import Annotation, Term


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Annotation
        fields = ("explanation", "locale", "term")


class RetrieveResponseSerializer(serializers.ModelSerializer):
    annotation = AnnotationSerializer()
    class Meta:
        model = Term
        field = ("name", "annotation", "images", "audio_url", "video_url")

