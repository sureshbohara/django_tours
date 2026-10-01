from django.db import models
from django.conf import settings

class LoginActivity(models.Model):
    DEVICE_TYPES = [
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
        ('tablet', 'Tablet'),
    ]

    # Django को User model सँग जोड्ने (Admin/User जे भए पनि मिल्छ)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='login_activities'
    )
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    browser = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES, default='desktop')
    
    login_at = models.DateTimeField(auto_now_add=True)
    logout_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-login_at']
        verbose_name = 'Login Activity'
        verbose_name_plural = 'Login Activities'

    def __str__(self):
        return f"{self.user} - {self.login_at}"