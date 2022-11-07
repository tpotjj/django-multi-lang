from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework .response import Response

from .models import Term
from .serializers import RetrieveResponseSerializer


# Create your views here.
class TermViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, pk=None):
        request_locales = request.headers.get("Accept-Language", settings.DEFAULT_TERM_LOCALE)
        locales = request_locales.split(";")

        term = get_object_or_404(Term, pk=pk) 
        if not term:
            return Response(status=404)
        term.annotations = term.get_annotation_locale_or_default(locales)
        response = RetrieveResponse(data=term)           
        serializer = RetrieveResponseSerializer(response)

        return Response(serializer.data)
