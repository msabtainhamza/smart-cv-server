from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from weasyprint import HTML

from smart_cv_server.settings import model
from src.api.cv_resume.serializers import CVResumeSerializer, DownloadCVResumeSerializer, ProfilePicSearializer
from src.apps.cv_resume.models import CVResume


class ResumeView(viewsets.ModelViewSet):
    queryset = CVResume.objects.all()
    serializer_class = CVResumeSerializer
    permission_classes = [AllowAny]


class DownloadCvResumeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DownloadCVResumeSerializer

    def get(self, request, *args, **kwargs):
        _id = kwargs.get('cv_resume_id')
        template_type = kwargs.get('template_type')
        cv_resume = get_object_or_404(CVResume, pk=_id)

        body = model.generate(gen_for='cv',type=template_type,object=cv_resume)
        cv_resume.body = body

        if cv_resume.prifile_picture:
            profile_ = cv_resume.prifile_picture.profile_pic.url
        else:
            profile_ = None
        profile_pic_url = request.build_absolute_uri(profile_)
        template = get_template(f'cv_resumes/{template_type}.html')
        html = template.render({'cv_resume': cv_resume, 'profile_pic_url': profile_pic_url})

        pdf_file = HTML(string=html).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv_resume.personal_info.full_name}.pdf"'
        return response


class CVResumeCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)

        serializer = CVResumeSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCVResumesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):

        serializer = CVResumeSerializer()
        cv_resumes = serializer.get_cv_resumes(id)
        return Response(cv_resumes)


class ImageUploadAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ProfilePicSearializer(data=request.data)
        print("IMAGE DATA .................................................")
        if serializer.is_valid():
            # print(serializer.data)

            instance = serializer.save()
            return Response({'id': instance.id, 'message': 'Image uploaded successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


