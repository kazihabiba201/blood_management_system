from rest_framework.routers import DefaultRouter
from .views import BloodBankViewSet, BloodDonationRequestViewSet

router = DefaultRouter()
router.register('bloodbanks', BloodBankViewSet)
router.register('donations', BloodDonationRequestViewSet)

urlpatterns = router.urls
