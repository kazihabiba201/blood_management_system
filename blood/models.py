from django.db import models
from accounts.models import CustomUser, BLOOD_GROUPS

class BloodBank(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_available = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return f"{self.name} ({self.blood_group})"


class BloodDonationRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.blood_group} ({self.status})"
