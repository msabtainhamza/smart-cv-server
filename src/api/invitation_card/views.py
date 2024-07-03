import os
from io import BytesIO

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from weasyprint import HTML, CSS
from xhtml2pdf import pisa

from smart_cv_server import settings
from src.api.invitation_card.serializers import InvitationSerializer, DownloadInvitationCardSerializer
from src.apps.invitation_card.models import Invitation


class InvitationCardView(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [AllowAny]


class DownloadInvitationCardView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DownloadInvitationCardSerializer

    def get(self, request, *args, **kwargs):
        _id = kwargs.get('invitation_id')
        template_type = kwargs.get('template_type')
        invitation_card = get_object_or_404(Invitation, pk=_id)

        template = get_template(f'invitation_cards/{template_type}.html')

        # Read the Bootstrap CSS file content
        css_path = os.path.join(settings.STATIC_URL, 'css/bootstrap.min.css')
        with open(css_path, 'r') as css_file:
            bootstrap_css = css_file.read()

        html_content = template.render({'invitation': invitation_card, 'bootstrap_css': bootstrap_css})

        # Create a PDF using WeasyPrint
        pdf_file = BytesIO()
        HTML(string=html_content).write_pdf(pdf_file, stylesheets=[CSS(string=bootstrap_css)])
        pdf_file.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{invitation_card.host.hostname}.pdf"'
        response.write(pdf_file.read())

        return response
class GetInvitationCardsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        serializer = InvitationSerializer()
        cv_resumes = serializer.get_cv_resumes(id)
        return Response(cv_resumes)