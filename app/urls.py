from django.urls import path
from . import views

urlpatterns = [
    # path('',views.contact, name='contact'),
    path('', views.aplicant_edit, name='aplicant_edit'),
    # path('', views.course_edit, name='course_edit'),
    # path('', views.home, name='home'),
    # path('new_aplicant/', views.new_aplicant, name='new_aplicant'),
    # path('edit_aplicant/', views.edit_aplicant, name='edit_aplicant'),
]