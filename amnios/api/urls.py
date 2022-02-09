from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgencyViewSet, SellerViewSet, BuyerViewSet, EstateAgentViewSet, EstateViewSet, VisitSlotViewSet

router = DefaultRouter()
router.register('agencies', AgencyViewSet, 'agency')
router.register('selleres', SellerViewSet, 'seller')
router.register('buyers', BuyerViewSet, 'buyer')
router.register('estate_agents', EstateAgentViewSet, 'estate_agent')
router.register('estate', EstateViewSet, 'estate')
router.register('visit_slots', VisitSlotViewSet, 'visit_slot')

urlpatterns = [
    path('', include(router.urls)),
]
