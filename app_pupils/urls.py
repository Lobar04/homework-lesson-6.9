from django.urls import path

from .views import pupils, pupil

urlpatterns = [
    path('pupils/',pupils,name = 'pupils_url'),
    path('pupils/<int:pupil_id>/', pupil, name='pupil'),
]