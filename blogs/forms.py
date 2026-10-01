from django import forms
from .models import Post
from categories.models import Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category', 'title', 'slug', 'image', 'excerpt', 'description',
            'meta_title', 'meta_description', 'is_featured', 'order_level', 'status'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Main blog content...'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }