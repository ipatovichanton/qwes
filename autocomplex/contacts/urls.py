from django.urls import path,include

urlspatterns=[
    path('contacts/',include('contacts.views'))
]