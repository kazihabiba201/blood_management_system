from django import forms
from .models import BloodDonationRequest, BLOOD_GROUPS
from blood.models import BloodBank

class BloodBankForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name', 'blood_group', 'units_available', 'city']
class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['blood_group', 'units']
        widgets = {
            'blood_group': forms.Select(choices=BLOOD_GROUPS, attrs={'class': 'form-control'}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
