"""collegewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from colleageapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',views.fun1),
    path('fit/',views.fun2),
    path('fit1/',views.fun3),
    path('jack/',views.fun4),
    path('fish/',views.fun5),
    path('sit/',views.fun6),
    path('sit1/',views.fun7),
    path('cheek/',views.fun8),
    path('def/',views.fun9),
    path('def1/',views.fun10),
    path('def2/',views.fun11)
    
]
