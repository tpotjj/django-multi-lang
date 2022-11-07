from django.contrib import admin

from .models import Annotation, Term
# Register your models here.

class AnnotationAdmin(admin.ModelAdmin):
    pass

class TermAdmin(admin.ModelAdmin):
    pass

admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Term, TermAdmin)

