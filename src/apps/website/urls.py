from django.urls import path

app_name = 'website'
from .views import (HomePageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

]
