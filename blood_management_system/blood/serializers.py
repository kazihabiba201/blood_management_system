from rest_framework import serializers
from accounts.models import CustomUser
from .models import BloodBank, BloodDonationRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'blood_group', 'city', 'is_donor']

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = '__all__'

class BloodDonationRequestSerializer(serializers.ModelSerializer):
    donor = UserSerializer(read_only=True)
    class Meta:
        model = BloodDonationRequest
        fields = '__all__'
