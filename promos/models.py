from django.db import models

class PromoCode(models.Model):
    DISCOUNT_TYPES = [
        ('percentage', 'Percentage (%)'),
        ('fixed', 'Fixed Amount ($)'),
    ]

    code = models.CharField(max_length=50, unique=True, help_text="e.g., SUMMER2024")
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, default='percentage')
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="e.g., 20 for 20% or 50 for $50")
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Minimum booking amount to apply (0 = No limit)")
    max_uses = models.PositiveIntegerField(default=0, help_text="Maximum times this code can be used (0 = Unlimited)")
    used_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateField(blank=True, null=True, help_text="Leave blank for no expiry")
    status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Promo Code'
        verbose_name_plural = 'Promo Codes'

    def __str__(self):
        return self.code

    @property
    def is_active(self):
        if not self.status:
            return False
        if self.max_uses > 0 and self.used_count >= self.max_uses:
            return False
        if self.expires_at and self.expires_at < self.created_at.date(): # Simplified check, better to compare with today
            from datetime import date
            if self.expires_at < date.today():
                return False
        return True