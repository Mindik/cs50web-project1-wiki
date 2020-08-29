from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki/", views.wikiIndex, name="wikiIndex"),
    path("rand", views.rand, name="rand"),
    path("search", views.search, name="search"),
    path("newpage", views.newPage, name="newPage"),
    path("editpage/<str:title>", views.editPage, name="editPage")
]
