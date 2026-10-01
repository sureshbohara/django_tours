from django.db import models

class Team(models.Model):
    ROLE_CHOICES = [
        ('office', 'Office Staff'),
        ('guide', 'Guide'),
        ('porter', 'Porter'),
    ]
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='office')
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='teams/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level']

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

    @property
    def image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/asset/images/noimage.png'