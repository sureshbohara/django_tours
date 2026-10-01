from django.db import models
from django.utils.text import slugify
from categories.models import Category 

class PostManager(models.Manager):
    def active(self):
        return self.filter(status=True)
    
    def ordered(self):
        return self.order_by('order_level', '-created_at')
    
    def featured(self):
        return self.filter(is_featured=True, status=True)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True, help_text="Brief excerpt/summary")
    description = models.TextField(help_text="Main blog content")
    
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True) 
    order_level = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['order_level', '-created_at']
        indexes = [
            models.Index(fields=['status', 'order_level', 'created_at']),
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