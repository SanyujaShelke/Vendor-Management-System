# vendors/views.py
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
# views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Vendor Management System!")


# Token Obtain and Refresh Views
token_obtain_view = TokenObtainPairView.as_view()
token_refresh_view = TokenRefreshView.as_view()


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
