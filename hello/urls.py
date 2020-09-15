from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tlek", views.tlek, name="tlek"),
    path("<str:name>", views.greet, name="greet")
]