from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from remeapp.views import *

router = routers.DefaultRouter() 
router.register(r"cells", CellsViewSet, basename='cells')
router.register(r"tags", TagsViewSet, basename='tags')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/v1/', include(router.urls)),
	path('api/v1/', include('rest_framework.urls')),
	path('api/v1/auth/', include('djoser.urls')), # djoser
	re_path(r'^auth/', include('djoser.urls.authtoken')), # djoser
]
