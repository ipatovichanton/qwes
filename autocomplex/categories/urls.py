from django.urls import path, include
from categories import views

urlpatterns=[
path('',views.categories),
path('moscow_detail',views.moscow_detail),
path('sliva_detail',views.sliva_detail),
path('volga_detail',views.volga_detail),
]