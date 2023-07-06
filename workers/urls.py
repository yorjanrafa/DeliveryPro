from django.urls import path
from django.contrib.auth import views as views_auth

from .views import editWorker, listActivityWorker, listWorker, newWorker, deleteWorker

urlpatterns = [
    path('list', listWorker, name="list"),
    path('new', newWorker, name="new"),
    path('edit/<id>', editWorker, name="edit"),
    path('delete/<id>', deleteWorker, name="delete"),
    path('list-activity/<id>', listActivityWorker, name="list-activity"),
]
