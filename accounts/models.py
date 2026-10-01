from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('status', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) # ✅ Superuser active हुनुपर्छ
        return self.create_user(email, password, **extra_fields)


class AdminUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    
    image = models.ImageField(upload_to='admin_profiles/', null=True, blank=True, default='noimage.png')
    
    status = models.BooleanField(default=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and str(self.image) != 'noimage.png':
            return self.image.url
        return '/static/asset/images/noimage.png'

    # ❌ FIX: तलका @property हरू हटाउनुहोस् (Delete गर्नुहोस्)
    # @property
    # def is_active(self):
    #     return self.status
    #
    # @property
    # def is_staff(self):
    #     return self.status


    def has_perm(self, perm, obj=None):
        return self.is_active 

    def has_module_perms(self, app_label):
        return self.is_active