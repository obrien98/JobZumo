from django.urls import path
from . import views

app_name = 'job'
urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),

]
