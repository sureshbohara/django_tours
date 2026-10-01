from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title', 'slug', 'icon', 'image', 'short_content', 'content',
            'meta_title', 'meta_description', 'meta_keywords',
            'show_in_menu', 'show_in_footer', 'is_featured', 'order_level', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., About Us'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi bi-info-circle'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'short_content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief summary of the page...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Main page content...'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma separated keywords'}),
            'show_in_menu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_in_footer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }