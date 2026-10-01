from django.db import models

class BannerManager(models.Manager):
    def active(self):
        return self.filter(status=True)
    
    def ordered(self):
        return self.order_by('order_level', '-created_at')

class Banner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BannerManager()

    class Meta:
        ordering = ['order_level', '-created_at']
        indexes = [
            models.Index(fields=['status', 'order_level', 'created_at']),
        ]

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/asset/images/noimage.png'