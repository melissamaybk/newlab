from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('update/<str:pk>/', views.updateContact, name="updatecontact"),
    path('searchnamephone', views.searchName, name="searchnamephone"),
    path('searchjob', views.searchJob, name="searchjob"),
    path('comparename', views.compareName, name="comparename"),
  
]