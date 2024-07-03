from django.urls import include, path
from rest_framework import routers

from src.api.invitation_card.views import InvitationCardView, DownloadInvitationCardView, GetInvitationCardsView

router = routers.DefaultRouter()
router.register(r'', InvitationCardView)
app_name = 'invitation_card'
urlpatterns = [
    path('', include(router.urls)),
    path('download/<int:invitation_id>/<str:template_type>', DownloadInvitationCardView.as_view(), name='download'),
    path('invitationcards/<int:id>', GetInvitationCardsView.as_view(), name='invitationcards')

]