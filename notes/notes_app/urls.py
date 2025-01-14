from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_note, name="add-note"),
    path("delete/<str:pk>/", views.delete_note, name="delete-note"),
    path("edit/<str:pk>/", views.edit_note, name="edit-note"),
    path("display/<str:pk>/", views.display_note, name="display-note"),
]