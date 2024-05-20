from django.urls import path
from master import views

urlpatterns = [
    path(r'getanalytics/', views.getanalytics),
]