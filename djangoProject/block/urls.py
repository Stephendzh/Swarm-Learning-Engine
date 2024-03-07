from . import views
from django.urls import path

urlpatterns = [
    path('user/', views.user_exist, name='user_exist'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('', views.home_page, name='home_page'),
    path('charts/', views.chart_page, name='charts'),
    path('new/', views.new_transaction, name='new_transaction'),
]