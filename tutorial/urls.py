"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('snippets/',views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/',views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name='snippet-highlight'),
]

