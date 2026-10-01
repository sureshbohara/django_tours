from django.db import models
from django.conf import settings
from django.utils.text import slugify  

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
    
    def ordered(self):
        return self.order_by('order_level', 'name')

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True) # blank=True राख्नुहोस् ताकि form मा नलेख्दा पनि error नआओस्
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    font_icon = models.CharField(max_length=100, blank=True, null=True)
    order_level = models.IntegerField(default=0)
    display_on = models.CharField(max_length=100, default='default')
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_categories')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_categories')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CategoryManager()

    class Meta:
        ordering = ['order_level', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/asset/images/noimage.png'