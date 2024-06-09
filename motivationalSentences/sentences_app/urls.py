from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhraseView.as_view(), name="phrase-view"),
]