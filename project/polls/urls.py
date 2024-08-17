from django.urls import path
from . import views

urlpatterns = [
    path("<int:sign_person_type>/", views.get_person_type_num),  # Переменная url в виде int
    path("<str:sign_person_type>/", views.get_person_type)       # Переменная url в виде str
]

