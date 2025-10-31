from django.contrib.auth.models import AbstractUser
from django.db import models


BLOOD_GROUPS = (
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
)

class CustomUser(AbstractUser):
    is_donor = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username

