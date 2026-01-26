from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    # Example:
    path('', views.home, name='home'),

    path('add_person', views.add_person, name='add_person'),
]