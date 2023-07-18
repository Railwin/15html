"""
URL configuration for roflanLITSO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from IvatMaslov.views import index
from IvatMaslov.views import index2
from IvatMaslov.views import index3
from IvatMaslov.views import index4
from IvatMaslov.views import index5


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('IvatMaslov.urls')),
    path('', index, name = "home1"),
    path('my2.html', index2),
    path('my3.html', index3),
     path('my4.html', index4),
      path('my5.html', index5)

]

