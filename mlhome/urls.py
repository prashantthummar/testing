from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name='index'),
    path('adduser/', views.AddUserDetail.as_view(), name='adduser'),
    path('emp/', views.Exp_csv),
]