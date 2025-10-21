from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class AssetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asset_requests')
    
    product = models.CharField(max_length=100)
    asset_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tentative_vendor = models.CharField(max_length=255, blank=True, null=True)
    required_by_date = models.DateField(verbose_name="Required By Date")
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.status}] {self.product} ({self.quantity}) by {self.user.username}"
