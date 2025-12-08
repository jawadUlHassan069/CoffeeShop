from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffee/<int:id>/', views.coffee_detail, name='coffee_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
    path('review/<int:coffee_id>/', views.add_review, name='add_review'),
]