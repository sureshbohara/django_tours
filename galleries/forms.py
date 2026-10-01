from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'display_on', 'image', 'alt', 'order_level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Everest Base Camp Trek'
            }),
            'display_on': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('default', 'Default'),
                ('gallery_page', 'Gallery Page') 
            ]),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/png, image/jpeg, image/webp'
            }), 
            
            'alt': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Group photo at Everest Base Camp (for SEO)'
            }),
            'order_level': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': 0, 
                'placeholder': '0 = Highest priority'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                (True, '✅ Active'), 
                (False, '❌ Inactive')
            ]),
        }