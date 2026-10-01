from django.db import models
from django.utils.text import slugify
from categories.models import Category

class Package(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    feature_image = models.ImageField(upload_to='packages/features/', blank=True, null=True)
    gallery = models.JSONField(default=list, blank=True)
    map = models.TextField(blank=True, null=True)
    
    trip_previous_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trip_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    group_size_price = models.JSONField(default=list, blank=True)
    
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    highlight_key = models.JSONField(default=list, blank=True)
    included_data = models.JSONField(default=list, blank=True)
    excluded_data = models.JSONField(default=list, blank=True)
    faqs = models.JSONField(default=list, blank=True)
    itinerary_data = models.JSONField(default=list, blank=True)
    
    general = models.JSONField(default=list, blank=True)
    lower_body = models.JSONField(default=list, blank=True)
    upper_body = models.JSONField(default=list, blank=True)
    footwear = models.JSONField(default=list, blank=True)
    accessories = models.JSONField(default=list, blank=True)
    activities = models.JSONField(default=list, blank=True)
    
    duration = models.CharField(max_length=100, blank=True, null=True)
    transportation = models.CharField(max_length=100, blank=True, null=True)
    trip_grading = models.CharField(max_length=100, blank=True, null=True)
    max_altitude = models.CharField(max_length=100, blank=True, null=True)
    accommodation = models.CharField(max_length=100, blank=True, null=True)
    meals = models.CharField(max_length=100, blank=True, null=True)
    best_season = models.CharField(max_length=100, blank=True, null=True)
    
    view_count = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    order_level = models.PositiveIntegerField(default=0)
    display_on = models.CharField(max_length=50, blank=True, null=True)
    
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category, related_name='packages', blank=True)

    class Meta:
        ordering = ['order_level', '-created_at']
        indexes = [models.Index(fields=['status', 'order_level'])]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/asset/images/noimage.png'

    @property
    def feature_image_url(self):
        return self.feature_image.url if self.feature_image and hasattr(self.feature_image, 'url') else '/static/asset/images/noimage.png'


class FixedDeparture(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='fixed_departures')
    start_date = models.DateField()
    end_date = models.DateField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_seats = models.PositiveIntegerField(default=0)
    booked_seats = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.package.name} - {self.start_date}"

    @property
    def available_seats(self):
        return max(0, self.max_seats - self.booked_seats)

    @property
    def current_price(self):
        # if discount_price छ भने त्यो देखाउने, other wise Package  regular price 
        return self.discount_price if self.discount_price else self.package.trip_price