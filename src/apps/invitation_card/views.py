import os
from io import BytesIO

from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string, get_template
from django.views.generic import TemplateView, DetailView
from xhtml2pdf import pisa

from src.apps.invitation_card.forms import CombinedForm
from src.apps.invitation_card.models import Invitation


class InvitationCardCreateView(TemplateView):
    template_name = 'invitation_card.html'

    def get_context_data(self, **kwargs):
        super(InvitationCardCreateView, self).get_context_data(**kwargs)
        context = super(InvitationCardCreateView, self).get_context_data(
            form=CombinedForm
        )

        return context

    def post(self, request, *args, **kwargs):
        combined_form = CombinedForm(request.POST)
        card = combined_form.save(request)
        _id = card.id

        if combined_form.is_valid():

            return HttpResponseRedirect(f"invitation_card/{_id}")
        else:
            pass


class InvitationCardTemplateView(TemplateView):
    def get_template_names(self):
        template_type = self.kwargs.get('template_type', 'default')
        return [f'invitation_cards/{template_type}.html']
    def get_context_data(self, **kwargs):
        _id = kwargs.get('id')
        invitation = get_object_or_404(Invitation, pk=_id)

        context = super(InvitationCardTemplateView, self).get_context_data(
            invitation=invitation
        )
        return context

    def post(self, request, *args, **kwargs):
        _id = kwargs.get('id')
        invitation = get_object_or_404(Invitation, pk=_id)
        template = get_template('required/example_template.html')
        html = template.render({'invitation': invitation})

        soup = BeautifulSoup(html, 'html.parser')
        pdf_html = str(soup.find('section'))

        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(pdf_html, dest=buffer)
        if pisa_status.err:
            return HttpResponse('PDF generation error!', status=500)

        pdf_data = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invitation_detail.pdf"'
        response.write(pdf_data)

        return response
