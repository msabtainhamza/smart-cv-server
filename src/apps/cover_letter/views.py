from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from smart_cv_server.settings import model
from src.apps.cover_letter.models import CoverLetter


class TemplateViewCoverLetter(TemplateView):
    def get_template_names(self):
        template_type = self.kwargs.get('template_type', 'default')
        return [f'cover_letters/{template_type}.html']

    def get_context_data(self, **kwargs):
        _id = kwargs.get('id')
        template_type = self.kwargs.get('template_type', 'default')

        cover_letter = get_object_or_404(CoverLetter, pk=_id)
        body =model.generate(gen_for="cover_letter",
                             type=template_type,
                             object=cover_letter)
        cover_letter.body = body
        context = super(TemplateViewCoverLetter, self).get_context_data(
            cover_letter=cover_letter
        )
        return context


