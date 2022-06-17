from django.urls import path

from webapp.views import article_create_view

urlpatterns = [
    path("", article_create_view),
]

