from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from src.apps.cover_letter.views import TemplateViewCoverLetter

app_name = 'cover_letter'
urlpatterns = [
    path('template/<int:id>/<str:template_type>', TemplateViewCoverLetter.as_view() , name="cover_letter")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)