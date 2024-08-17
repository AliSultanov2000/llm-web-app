from django.contrib import admin
from django.urls import include, path
# from polls.views import 

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]