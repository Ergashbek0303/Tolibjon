from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='home'),
    path("1", views.index1,name='product1'),
    path("2", views.index2,name='product2'),
    path("3", views.index3, name='product3'),
    path("4", views.index4,name='product4'),
    path('baskets/add/<int:product_id>/', views.basket_add,name='basket_add'),
    path('baskets/minus/<int:product_id>/', views.basket_minus,name='basket_minus'),
    path('basket', views.basket,name='basket'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove,name='basket_remove'),
]