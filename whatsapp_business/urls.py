from django.urls import path, include
from whatsapp_business import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'job', views.UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('msg/', views.WhatsAppWrapper.as_view()),
    # path('job/', views.UserViewSet.as_view())
]