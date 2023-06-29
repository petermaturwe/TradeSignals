from django.urls import path
from . import views
from .views import loginview,logoutview

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('payment/', views.payment, name='payment'),
]
urlpatterns += staticfiles_urlpatterns()