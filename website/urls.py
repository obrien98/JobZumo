"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from job import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job_views.index, name = 'index'),
    path('BusinessRegistration', job_views.business_registration, name = 'business_registration'),
    path('search_results', job_views.search_results, name = 'search_results'),
    path('account/', include('account.urls')),
    path('dashboard/', job_views.dashboard, name = 'dashboard'),
    path('post_job/', job_views.post_job, name = 'post_job'),
    path('edit/<int:pk>/', job_views.JobUpdateView.as_view(), name='edit_job'),
    path('delete/<int:pk>/', job_views.JobDeleteView.as_view(), name='delete_job'),
    path('emailSubscription/', job_views.job_seeker_email, name='email_subscription'),

]
