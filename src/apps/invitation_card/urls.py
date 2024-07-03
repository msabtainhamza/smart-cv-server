from django.urls import path

from src.apps.invitation_card.views import InvitationCardCreateView , InvitationCardTemplateView

app_name = 'invitation_card'
urlpatterns = [
    path('invition_card_create', InvitationCardCreateView.as_view(), name='invitation_card_create'),
    path('template/<str:id>/<str:template_type>', InvitationCardTemplateView.as_view(),name='invitation_card')
]

