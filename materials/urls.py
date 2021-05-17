from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MaterialListView.as_view(), name='list'),
    path('add/<int:pk>',MaterialCreateView.as_view(),name='add'),
    path('update/<int:pk>',MaterialUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',MaterialDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>',MaterialDetailView.as_view(),name='detail'),
]


