from django import forms
from .models import SiteSetting

class SettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        exclude = ['process_item', 'work_item', 'counter_item']
        
        widgets = {
            'system_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'extra_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'extra_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'opening_hr': forms.TextInput(attrs={'class': 'form-control'}),
            'work_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'google_map': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'footer_copyright': forms.TextInput(attrs={'class': 'form-control'}),
            
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control'}),
            'google': forms.URLInput(attrs={'class': 'form-control'}),
            'yelp': forms.URLInput(attrs={'class': 'form-control'}),
            
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control'}),
            'loader': forms.FileInput(attrs={'class': 'form-control'}),
            'footer_gateway_img': forms.FileInput(attrs={'class': 'form-control'}),
            'bg_image': forms.FileInput(attrs={'class': 'form-control'}),
            'breadcrumb': forms.FileInput(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            
            'meta_author': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            'info1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info3': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info4': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info5': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info6': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'info7': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            'mail_transport': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_host': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_port': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail_username': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_password': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_encryption': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_from': forms.EmailInput(attrs={'class': 'form-control'}),
            'mail_from_name': forms.TextInput(attrs={'class': 'form-control'}),
            
            'google_analytic_id': forms.TextInput(attrs={'class': 'form-control'}),
            'google_client_id': forms.TextInput(attrs={'class': 'form-control'}),
            'google_client_secret': forms.TextInput(attrs={'class': 'form-control'}),
            'google_redirect': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_analytic_id': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_client_id': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_client_secret': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_redirect': forms.URLInput(attrs={'class': 'form-control'}),
            'recaptcha_site_key': forms.TextInput(attrs={'class': 'form-control'}),
            'recaptcha_secret_key': forms.TextInput(attrs={'class': 'form-control'}),
            
            'process_title': forms.TextInput(attrs={'class': 'form-control'}),
            'process_sub_title': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'work_title': forms.TextInput(attrs={'class': 'form-control'}),
            'work_sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'counter_title': forms.TextInput(attrs={'class': 'form-control'}),
            'counter_sub_title': forms.TextInput(attrs={'class': 'form-control'}),
        }