from django import forms
from .models import PromoCode

class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount_type', 'discount_value', 'min_amount', 'max_uses', 'expires_at', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., DASHAIN50', 'style': 'text-transform: uppercase;'}),
            'discount_type': forms.Select(attrs={'class': 'form-select'}),
            'discount_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'e.g., 20 or 50'}),
            'min_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0 = No minimum'}),
            'max_uses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0 = Unlimited'}),
            'expires_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }