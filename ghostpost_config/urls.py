"""ghostpost_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ghostpost_app import views

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('addpost/', views.addpost_view, name='addpost'),
    path('boasts/', views.boasts_view, name='boasts'),
    path('roasts/', views.roasts_view, name='roasts'),
    path('upvote/<int:upvote_id>/', views.upvote_view, name='upvote'),
    path('downvote/<int:downvote_id>/', views.downvote_view, name='downvote'),
    path('sortedvotes/', views.sortbyvotescore_view, name='sortedvotes'),
    path('delete/<int:deletepost_id>/', views.delete_view, name='delete_post'),
    path('privatepost/<int:ps_key>/', views.privatepost_view, name='private_post'),
    path('admin/', admin.site.urls),
]
