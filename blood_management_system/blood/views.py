from rest_framework import viewsets, permissions
from .models import BloodBank, BloodDonationRequest
from .serializers import BloodBankSerializer, BloodDonationRequestSerializer

class BloodBankViewSet(viewsets.ModelViewSet):
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer
    permission_classes = [permissions.IsAdminUser]

class BloodDonationRequestViewSet(viewsets.ModelViewSet):
    queryset = BloodDonationRequest.objects.all()
    serializer_class = BloodDonationRequestSerializer

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)

