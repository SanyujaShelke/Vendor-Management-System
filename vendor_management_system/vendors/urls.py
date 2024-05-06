# vendors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListView.as_view(), name='vendor-list'),
    # Other URL patterns...
]
