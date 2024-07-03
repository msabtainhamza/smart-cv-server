from django.urls import include, path
from .docs import get_swagger_doc_schema_view

app_name = 'api'
urlpatterns = []

""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html --------------------------------------- """

schema_view = get_swagger_doc_schema_view()
urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

""" MAIN URLS ------------------------------------------------------------------------------------------------------ """

""" Version 1 of the API ------------------------------------------------------------------------------------------- """
urlpatterns += [

    # MAIN URLS

    path('cv_resume/', include('src.api.cv_resume.urls', namespace='cv_resume/')),
    path('invitation_card/', include('src.api.invitation_card.urls', namespace='invitation_card')),
    path('cover_letter/', include('src.api.cover_letter.urls', namespace='cover_letter')),
    # USER
    path('accounts/', include('src.api.accounts.urls', namespace='accounts')),

]
