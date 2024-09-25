
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("base", views.base, name='Base'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("", views.table, name='table'),
    path("form", views.form, name='form'),
    path("form/edit/<pk>", views.edit, name='edit'),
    path("form/delete/<pk>", views.delete, name="delete")
]
