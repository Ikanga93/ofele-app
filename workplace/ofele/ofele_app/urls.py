# IMport the necessary modules to call the view functions when the URL is requested.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.moderation_schedule, name='moderation_schedule'),
]