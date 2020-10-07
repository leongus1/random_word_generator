from django.urls import path
from . import views

urlpatterns = [
    path('', views.re_direct),
    path('random_word/reset/', views.reset),
    path('random_word/', views.rand),
    
]