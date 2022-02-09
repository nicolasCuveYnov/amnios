from rest_framework import serializers
from .models import Agency, Seller, Buyer, EstateAgent, Estate, VisitSlot


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class EstateAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateAgent
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'


class VisitSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitSlot
        fields = '__all__'
