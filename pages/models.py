from django.db import models
from django.utils.text import slugify

class PageManager(models.Manager):
    def active(self):
        return self.filter(status=True)
    
    def ordered(self):
        return self.order_by('order_level', '-created_at')
    
    def in_menu(self):
        return self.filter(show_in_menu=True, status=True)
    
    def in_footer(self):
        return self.filter(show_in_footer=True, status=True)

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., bi bi-info-circle")
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    short_content = models.CharField(max_length=500, blank=True, null=True, help_text="Brief excerpt/summary")
    content = models.TextField(blank=True, null=True)
    
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    show_in_menu = models.BooleanField(default=False)
    show_in_footer = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    order_level = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PageManager()

    class Meta:
        ordering = ['order_level', '-created_at']
        indexes = [
            models.Index(fields=['status', 'order_level', 'created_at']),
            models.Index(fields=['show_in_menu']),
            models.Index(fields=['show_in_footer']),
            models.Index(fields=['is_featured']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/asset/images/noimage.png'