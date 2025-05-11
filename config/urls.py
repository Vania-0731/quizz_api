"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración de Django
    path('api/', include('quizzes.urls')),  # Incluimos las URLs de la aplicación quizzes
    path('api/', include('categories.urls')), # Incluimos las URLs de la aplicación categories
    path('api-auth/', include('rest_framework.urls')), # Autenticación de la API de DRF
    path('api/analytics/', include('analytics.urls')),
    path('api/users/', include('users.urls')),
]
