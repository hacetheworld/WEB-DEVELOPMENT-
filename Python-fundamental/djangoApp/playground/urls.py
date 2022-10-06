from django.urls import path
from . import views
urlpatterns = [
    path("", views.say_hello),
    path("about", views.about),
    path("services", views.services),
    path("contact", views.contact)
]
