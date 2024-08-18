from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # Динамические url (в них роуты могут меняться)
    path("<int:sign_person_type>/", views.get_person_type_num),  # Переменная url в виде int
    path("<str:sign_person_type>/", views.get_person_type, name="polls_name")       # Переменная url в виде str
]
