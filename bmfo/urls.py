from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', join, name='signup'),
    path('login/', login, name='login'),
    path('userview/', userview, name='userview'),
    path('getproduct/', getProduct, name='getproduct'),
    path('add/',addProduct),
    path('user/',OAuth),
    path('all/',allProduct)
]