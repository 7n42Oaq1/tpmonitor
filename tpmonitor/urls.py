"""tpmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from monitor import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^login/',views.user_login,name="login"),
    url(r'^homepage/',views.homepage,name="homepage"),
    url(r'^devicemanage/',views.device_manage,name="dvmanage"),
    url(r'^mydevice/',views.my_device,name="mydevice"),
    url(r'^logout/',views.user_logout,name="logout"),
    url(r'^edit/(?P<name>t[0-9]+)/',views.edit_device,name="edit"),
]
