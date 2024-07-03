from src.apps.cover_letter.models import CoverLetter

from django.contrib import admin

@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'name','id')
    search_fields = ('user', 'name')
