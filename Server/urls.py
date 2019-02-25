"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from Consulta.SGR.Consumo.TrafoA.api.viewsets import trafoAViewSet
# from testCom.api.viewsets import testComViewSet

# router = routers.DefaultRouter()
# router.register(r'trafoA', trafoAViewSet)
# router.register(r'testCom', testComViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls),
# ]

from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from testCom.views import raw_sql_query
from Consulta.SGR.Consumo.TrafoA.api.viewsets import trafoAViewSet
from rest_framework import routers
from testCom.api.viewsets import testComViewSet

router = routers.DefaultRouter()
router.register(r'testCom', testComViewSet)
router.register(r'trafoA', trafoAViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^consulta/$', raw_sql_query),
]
