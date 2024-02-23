"""hostel1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('userreg', views.userreg,name='reg1'),
    path('login',views.login1234,name='login1234'),
    path('base',views.base,name='base'),
    path('base2',views.base2,name='base2'),
    path('search',views.search,name='search'),
    path('logout',views.logout,name='logout'),
    path('adminreg',views.adminreg,name='adminreg'),
    path('adminlogin',views.adminlogin1234,name='adminlogin'),
    path('admin_hostel',views.admin_hostel,name='admin_hostel'),
    path('hosteladd',views.hosteladd,name='hosteladd'),
    path('hostel_update/<int:h_id>',views.hostel_update,name='hostel_update'),
    path('user_submit/<int:h_id>',views.user_submit,name='user_submit'),
    path('del_booking_single/<str:HName>',views.del_booking_single,name='del_booking_single'),
    path('display_session',views.display_session,name='session'),
    path('confirm',views.confirm,name='confirm'),
]