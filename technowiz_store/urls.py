from django.contrib import admin
from django.urls import path
from products.views import product_list, product_detail , add_review
from leads.views import lead_create, lead_thank_you

urlpatterns = [
    path('admin/', admin.site.urls),

    # Product pages
    path('', product_list, name='product_list'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<slug:slug>/review/', add_review, name='add_review'),

    # Lead form
    path('request/<int:product_id>/', lead_create, name='lead_create'),
    path('thank-you/', lead_thank_you, name='lead_thank_you'),
]
