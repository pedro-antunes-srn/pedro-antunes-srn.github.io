from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path( 'nayara/<aniversario>/', views.post_detail, name='post_detail'),
 
]