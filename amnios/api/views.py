from rest_framework import viewsets

from .models import Agency, Seller, Buyer, EstateAgent, Estate, VisitSlot
from .serializers import AgencySerializer, SellerSerializer, BuyerSerializer, EstateAgentSerializer, EstateSerializer, VisitSlotSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class AgencyViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = AgencySerializer
    queryset = Agency.objects.all()


class SellerViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class BuyerViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()


class EstateAgentViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = EstateAgentSerializer
    queryset = EstateAgent.objects.all()


class EstateViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = EstateSerializer
    queryset = Estate.objects.all()


class VisitSlotViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = VisitSlotSerializer
    queryset = VisitSlot.objects.all()
