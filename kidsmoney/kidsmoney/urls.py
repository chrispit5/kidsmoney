"""kidsmoney URL Configuration

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
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
 	path('expense_detail/<int:id>', views.expense_detail, name='expense_detail'),   
 	path('add_expense/<int:id>', views.add_expense, name='add_expense'),
 	path('delete_expense/<int:id>', views.delete_expense, name='delete_expense'),
 	path('authenticate/', include('authenticate.urls')),
]
