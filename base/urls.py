from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('topics/', views.topics, name='topics'),
    path('topics/ArraysAndDateStructures/', views.ArraysAndDateStructures, name='ArraysAndDateStructures'),
    path('topics/stacksAndQueues/', views.stacksAndQueues, name='stacksAndQueues'),
    path('topics/twoPointers/', views.twoPointers, name='twoPointers'),
    path('topics/advancedGraphs/', views.advancedGraphs, name='advancedGraphs'),
    path('topics/backtracking/', views.backtracking, name='backtracking'),
    path('topics/ddp/', views.ddp, name='ddp'),
    path('topics/binarySearch/', views.binarySearch, name='binarySearch'),
    path('topics/bitManipulation/', views.bitManipulation, name='bitManipulation'),
    path('topics/ddptwo/', views.ddptwo, name='ddptwo'),
    path('topics/graphs/', views.graphs, name='graphs'),
    path('topics/greedy/', views.greedy, name='greedy'),
    path('topics/heaps/', views.heaps, name='heaps'),
    path('topics/intervals/', views.intervals, name='intervals'),
    path('topics/linkedList/', views.linkedList, name='linkedList'),
    path('topics/mathAndgeometry/', views.mathAndgeometry, name='mathAndgeometry'),
    path('topics/slidingWindow/', views.slidingWindow, name='slidingWindow'),
    path('topics/tries/', views.tries, name='tries'),
    path('topics/trees/', views.trees, name='trees'),
    path('social_providers_page/', views.social_providers_page, name='social_providers_page'),
    path('subscribe/', views.subscribe, name='subscribe'),
]