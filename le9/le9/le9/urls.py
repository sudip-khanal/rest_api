
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',views.StudentApi,basename='studentapi')
#read only viewset url
#router.register('studentapi',views.StudentReadOnlyViewset,basename='studentapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
  
]