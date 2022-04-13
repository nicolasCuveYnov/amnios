from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgencyViewSet, SellerViewSet, BuyerViewSet, EstateAgentViewSet, EstateViewSet, VisitSlotViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('agencies', AgencyViewSet, 'agency')
router.register('sellers', SellerViewSet, 'seller')
router.register('buyers', BuyerViewSet, 'buyer')
router.register('estate_agents', EstateAgentViewSet, 'estate_agent')
router.register('estates', EstateViewSet, 'estate')
router.register('visit_slots', VisitSlotViewSet, 'visit_slot')

urlpatterns = [
    path('', include(router.urls)),
    path('authToken/', obtain_auth_token, name='authToken')
]
