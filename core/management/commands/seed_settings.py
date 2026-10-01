from django.core.management.base import BaseCommand
from settings.models import SiteSetting
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the Site Settings with default configuration'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Site Settings...')

        current_year = datetime.now().year

        SiteSetting.objects.update_or_create(
            pk=1, 
            defaults={
                # --- General Info ---
                'system_name': 'Ez Property',
                'email': 'support@ezproperty.com',
                'extra_email': 'booking@ezproperty.com',
                'phone': '+977-1-XXXXXXX',
                'extra_phone': '+977-98XXXXXXXX', 
                'address': 'Kathmandu, Nepal',
                'opening_hr': 'Sun - Fri: 9AM - 6PM',
                'work_hours': 'Your gateway to authentic Nepali hospitality.',
                'footer_copyright': f'© {current_year} Ez Property. All Rights Reserved.',
                'google_map': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3532.0284987496536!2d85.32405831506056!3d27.717245933190117!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb19a8b5b88e43%3A0x6d64b8f8b8b8b8b8!2sKathmandu!5e0!3m2!1sen!2snp!4v1620000000000', 

                # --- Social Links ---
                'facebook': 'https://facebook.com/ezproperty',
                'twitter': 'https://twitter.com/ezproperty',
                'linkedin': 'https://linkedin.com/company/ezproperty',
                'instagram': 'https://instagram.com/ezproperty',
                'youtube': None,
                'google': None,
                'yelp': None,

                # --- Media ---
                'favicon': None,
                'logo': None,
                'loader': None,
                'footer_gateway_img': None,
                'bg_image': None,
                'breadcrumb': None,
                'image1': None, 
                'image2': None,

                # --- SEO Meta Data ---
                'meta_author': 'Ez Property',
                'meta_title': 'Ez Property | Find Premium Homestays & Rentals in Nepal',
                'meta_keywords': 'nepal property, homestay nepal, kathmandu apartment, pokhara rental, nepal travel, book hotel nepal',
                'meta_description': 'Discover authentic Nepali hospitality with Ez Property. Book premium homestays, city apartments, and mountain retreats across Nepal.',

                # --- Info Texts ---
                'info1': 'Your Gateway to Authentic Nepali Hospitality',
                'info2': 'Founded in Kathmandu, Ez Property is dedicated to connecting travelers with unique homes, breathtaking landscapes, and genuine local experiences.',
                'info3': 'Our mission is to empower local communities by providing a platform that promotes sustainable tourism, making authentic Nepali homestays accessible to the world.',
                'info4': 'Your gateway to authentic Nepali hospitality. Find your perfect mountain retreat, city apartment, or jungle lodge.',
                'info5': 'Secure Online Payments',
                'info6': '24/7 Local Support',
                'info7': None,

                # --- SMTP / Mail ---
                'mail_transport': 'smtp',
                'mail_host': 'smtp.gmail.com',
                'mail_port': 587, 
                'mail_username': 'ezbooking42@gmail.com',
                'mail_password': 'uqxr fnvu uznf zisi',
                'mail_encryption': 'tls',
                'mail_from': 'noreply@ezproperty.com',
                'mail_from_name': 'Ez Property',
                'smtp_check': True,

                # --- ReCaptcha ---
                'recaptcha_site_key': '', 
                'recaptcha_secret_key': '', 
                'is_recaptcha': False,

                # --- Analytics ---
                'google_analytic_id': '',
                'facebook_analytic_id': '',

                # --- Social Login ---
                'facebook_client_id': '',
                'facebook_client_secret': '',
                'facebook_redirect': '',
                'is_facebook': False,
                'google_client_id': '',
                'google_client_secret': '',
                'google_redirect': '',
                'is_google': False,

                # --- JSON Fields ---
                'process_title': 'Adventure handled with care, from Kathmandu to the summit',
                'process_sub_title': 'We are a team of mountain people — born, raised, and trained in the Himalayas.',
                'process_item': [
                    {
                        'icon': 'bi bi-people-fill', 
                        'title': 'Local Sherpa & Gurung Guides', 
                        'content': 'Born and raised in the mountains, our guides know every trail, village, and monastery by heart.'
                    },
                    {
                        'icon': 'bi bi-shield-check', 
                        'title': 'Safety First, Always', 
                        'content': 'Comprehensive first-aid training, oxygen support, insurance, and emergency evacuation plans on every trip.'
                    },
                    {
                        'icon': 'bi bi-map', 
                        'title': 'Handcrafted Itineraries', 
                        'content': 'No cookie-cutter tours. Every route is designed around your pace, interests, and schedule.'
                    },
                    {
                        'icon': 'bi bi-cash-coin', 
                        'title': 'Fair & Transparent Pricing', 
                        'content': 'Clear costs, no hidden fees, and fair wages for every porter, guide, and mountain community we work with.'
                    }
                ],

                'work_title': 'Become a Host',
                'work_sub_title': 'Ready to earn from your property? Upgrade your account now to access the host dashboard.',
                'work_item': [
                    {'icon': 'fa-solid fa-user-plus', 'title': 'Submit Verification Details', 'content': 'Provide your PAN and Citizenship number for legal verification.'},
                    {'icon': 'fa-solid fa-list-check', 'title': 'Wait for Admin Approval', 'content': 'Our team will verify your documents. This usually takes 24-48 hours.'},
                    {'icon': 'fa-solid fa-sliders', 'title': 'List Your Property', 'content': 'Once approved, add your property details, location, amenities, and photos.'},
                    {'icon': 'fa-solid fa-door-open', 'title': 'Welcome Your Guests', 'content': 'Your listing goes live! Start receiving bookings and earning income.'}
                ],

                'counter_title': 'Why Book With Us',
                'counter_sub_title': 'Trusted by Travelers Across the Globe',
                'counter_item': [
                    {'icon': 'fa-solid fa-building', 'title': '500+', 'content': 'Properties Listed'},
                    {'icon': 'fa-solid fa-users', 'title': '10K+', 'content': 'Happy Travelers'},
                    {'icon': 'fa-solid fa-location-dot', 'title': '15+', 'content': 'Cities Covered'},
                    {'icon': 'fa-solid fa-star', 'title': '4.8', 'content': 'Average Rating'}
                ],
            }
        )

        self.stdout.write(self.style.SUCCESS('✅ Site Settings seeded successfully!'))