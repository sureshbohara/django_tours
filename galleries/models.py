from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    display_on = models.CharField(max_length=100, default='default')
    image = models.ImageField(upload_to='galleries/')
    alt = models.CharField(max_length=255, blank=True, null=True)
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/asset/images/noimage.png'