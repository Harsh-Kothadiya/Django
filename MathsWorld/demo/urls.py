"""
URL configuration for demo project.

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
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('si',views.si,name='si'),
    path('si_result',views.si_result,name='si_result'),
    path('ci',views.ci,name='ci'),
    path('ci_result',views.ci_result,name='ci_result'),
    path('hcf_lcm',views.hcf_lcm,name='hcf_lcm'),
    path('hcf_lcm_result',views.hcf_lcm_result,name='hcf_lcm_result'),
    path('profit_loss',views.profit_loss,name='profit_loss'),
    path('profit_loss_result',views.profit_loss_result,name='profit_loss_result'),
    path('km_to_m',views.km_to_m,name='km_to_m'),
    path('km_to_m_result',views.km_to_m_result,name='km_to_m_result'),
    path('km_to_cm',views.km_to_cm,name='km_to_cm'),
    path('km_to_cm_result',views.km_to_cm_result,name='km_to_cm_result'),
    path('d_to_b',views.d_to_b,name='d_to_b'),
    path('d_to_b_result',views.d_to_b_result,name='d_to_b_result'),
    path('d_to_o',views.d_to_o,name='d_to_o'),
    path('d_to_o_result',views.d_to_o_result,name='d_to_o_result'),
    path('d_to_h',views.d_to_h,name='d_to_h'),
    path('d_to_h_result',views.d_to_h_result,name='d_to_h_result'),


]
