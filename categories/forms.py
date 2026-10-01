from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent', 'name', 'slug', 'excerpt', 'description', 'image', 
            'font_icon', 'order_level', 'display_on', 'meta_keywords', 
            'meta_description', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g., Electronics'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., electronics'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary shown in listings...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detailed content for the category page...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/png, image/jpeg, image/webp'}),
            'font_icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi bi-shop'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0 = Highest priority'}),
            
    
            'parent': forms.Select(attrs={'class': 'form-select'}),
            
            'display_on': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('default', 'Default'), 
                ('header', 'Header'), 
                ('footer', 'Footer')
            ]),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma separated keywords'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'SEO description (150-160 chars)'}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[
                (True, '✅ Active'), 
                (False, '❌ Inactive')
            ]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
  
        if self.instance and self.instance.pk:
            self.fields['parent'].queryset = Category.objects.exclude(pk=self.instance.pk).filter(parent__isnull=True).order_by('name')
        else:
            self.fields['parent'].queryset = Category.objects.filter(parent__isnull=True).order_by('name')
        

        self.fields['parent'].empty_label = "None (Root Category)"