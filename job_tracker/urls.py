"""
URL configuration for job_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import settings
from django.conf.urls.static import static 
from tracker.views import job_list, job_edit, job_delete, job_add

urlpatterns = [
    path('', job_list, name='job_list'),
    path('add/', job_add, name='job_add'),
    path('edit/<int:pk>/', job_edit, name='job_edit'),
    path('delete/<int:pk>/', job_delete, name='job_delete'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
