from django.urls import path
from . import views
from .views import loginview,logoutview

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name="base"),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('payment/', views.payment, name='payment'),
    path('stock/', views.stock_signals, name='stock_signals'),
    path('forex/', views.forex_signals, name='forex_signals'),
    path('crypto/', views.crypto_signals, name='crypto_signals'),
]
urlpatterns += staticfiles_urlpatterns()