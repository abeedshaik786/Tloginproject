"""tproject URL Configuration

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
from django.conf.urls import url,include
from tapp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home/',views.home),
    url(r'^java/',views.java),
    url(r'^python/',views.python),
    url(r'^c/',views.c),
    url(r'^adds/',views.add_student),
    url(r'^addt/',views.add_teacher),
    #url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^treg/',views.teacher_reg),
    url(r'^tlog/',views.teacher_log),
    url(r'^sreg/',views.student_reg),
    url(r'^slog/', views.student_log),
    url(r'^reg/',views.register),
    url(r'^log/', views.login),
    url(r'^logout/',views.logout),
    url(r'^add/',views.add_questions),
    url(r'^genarate/',views.genarate),

]
