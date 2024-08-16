from django.contrib import admin
from django.urls import include, path
from polls.views import leo, wolf

urlpatterns = [
    # path("", include("polls.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("polls/leo/", leo), 
    path("polls/wolf/", wolf)
]