from django.urls import path
from . import views

urlpatterns = [
    path("", views.Indexview.as_view()),
    path("register/", views.RegisterView.as_view()),
 #   path("savedata/", views.save_data)
]