from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('p/<slug:slug>/', views.product_detail, name='product_detail'),
    path('p/<slug:slug>/review/', views.add_review, name='add_review'),
    # path('cart/', views.cart_view, name='cart'),
    # path('checkout/', views.checkout_view, name='checkout'),
    # path('razorpay/create-order/', views.razorpay_create_order, name='razorpay_create_order'),
    # path('download/<int:order_item_id>/<uuid:token>/', views.download_product, name='download_product'),
]
