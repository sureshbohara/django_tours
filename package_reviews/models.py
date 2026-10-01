from django.db import models
from packages.models import Package

class PackageReview(models.Model):
    RATING_CHOICES = [(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]

    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField()
    status = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Package Review'
        verbose_name_plural = 'Package Reviews'

    def __str__(self):
        return f"{self.name} - {self.package.name} ({self.rating}★)"