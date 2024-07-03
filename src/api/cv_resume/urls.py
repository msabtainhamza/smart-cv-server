from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from smart_cv_server import settings
from .views import ResumeView, DownloadCvResumeView, CVResumeCreateView, GetCVResumesView, ImageUploadAPIView

app_name = 'cv_resume'

router = routers.DefaultRouter()
router.register(r'', ResumeView)

urlpatterns = [
                  path('', include(router.urls)),
                  path('download/<int:cv_resume_id>/<str:template_type>', DownloadCvResumeView.as_view(), name='download'),
                  path('create', CVResumeCreateView.as_view(), name='create'),
                  path('cvresumes/<int:id>', GetCVResumesView.as_view(), name='cvresumes'),
                  path('upload_image', ImageUploadAPIView.as_view(), name='image_upload'),


              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
