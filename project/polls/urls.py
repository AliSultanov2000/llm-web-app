from django.urls import path
from . import views

urlpatterns = [
    path("<sign_person_type>/", views.get_person_type)
]

