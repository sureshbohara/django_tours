from django import forms
from .models import Package, FixedDeparture
from categories.models import Category

class PackageForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Package
        fields = [
            'name', 'slug', 'image', 'feature_image', 'excerpt', 'description', 'content',
            'duration', 'max_altitude', 'best_season', 'meals', 'accommodation', 
            'transportation', 'trip_grading', 'activities',
            'meta_title', 'meta_keywords', 'meta_description', 'trip_previous_price', 
            'trip_price', 'order_level', 'display_on', 'status', 'categories'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g., Everest Base Camp Trek'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'feature_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '14 Days'}),
            'max_altitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5,545m'}),
            'best_season': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mar - May'}),
            'meals': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'B/L/D'}),
            'accommodation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tea House'}),
            'transportation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flight'}),
            'trip_grading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Moderate'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'trip_previous_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'trip_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
             'display_on': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', 'Select Display Option'), 
                ('default', 'Default'), 
                ('recommended', '⭐ Recommended'), 
                ('popular', '🔥 Popular'), 
                ('upcoming', '📅 Upcoming')
            ]),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }

class FixedDepartureForm(forms.ModelForm):
    class Meta:
        model = FixedDeparture
        fields = ['package', 'start_date', 'end_date', 'discount_price', 'max_seats', 'description', 'status']
        widgets = {
            'package': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discount_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'max_seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('active', '✅ Active'), ('cancelled', '❌ Cancelled'), ('completed', '✔️ Completed')
            ]),
        }