from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'address', 'rating', 'review', 'content', 'image', 'display_on', 'order_level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., John Doe'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., john@example.com'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Kathmandu, Nepal'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': 1, 
                'max': 5,
                'placeholder': '1 to 5'
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Short review title or summary (e.g., Amazing Experience!)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Detailed review content about your experience...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/png, image/jpeg, image/webp'
            }), 
            
            'display_on': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('default', 'Default'), 
                ('home', 'Home'),
                ('trekking', 'Trekking'),
                ('tours', 'Tours')
            ]),
            
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