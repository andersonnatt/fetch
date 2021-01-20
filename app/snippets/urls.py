from django.urls import path

from .views import Snippet


urlpatterns = [
    path("api/snippets/", Snippet.as_view()),
]