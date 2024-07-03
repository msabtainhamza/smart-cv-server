from django.core.serializers import serialize
from django.views.generic import TemplateView

from src.apps.cover_letter.models import CoverLetter
from src.apps.cv_resume.models import CVResume
from src.apps.invitation_card.models import Invitation



class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cv_resume'] = serialize('json', CVResume.objects.all())
        context['cover_letter'] = serialize('json', CoverLetter.objects.all())
        context['invitation'] = serialize('json', Invitation.objects.all())
        return context