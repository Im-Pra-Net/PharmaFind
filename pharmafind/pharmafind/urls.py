"""pharmafind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pages.views import account_redirect, home_view, pharmamanage, tohome, search, drugview
from testapp.views import testview
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', tohome, name='home'),
    path('search/', search, name='search'),
    path('test/', testview, name='test'),
    path('login/', LoginView.as_view()),
    path('accounts/', include("django.contrib.auth.urls")),
    path('medicineview/', drugview, name='medicineview'),
    path('pharmamanage/', pharmamanage, name='pharmamanage'),
    path('accounts/profile/', account_redirect, name='account-redirect')
]
