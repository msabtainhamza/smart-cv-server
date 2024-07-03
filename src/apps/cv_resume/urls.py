from django.urls import path

from src.apps.cv_resume.views import PersonalInfoView, CVResumeView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'cv_resume'
urlpatterns = [
    path('create/', PersonalInfoView.as_view(), name="create"),
    path('template/<int:id>/<str:template_type>', CVResumeView.as_view() , name="template")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)