from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('topics/', views.topics, name='topics'),
    path('social_providers_page/', views.social_providers_page, name='social_providers_page'),
]