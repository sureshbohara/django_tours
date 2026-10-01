from django.core.management.base import BaseCommand
from pages.models import Page 

class Command(BaseCommand):
    help = 'Seeds the Page table with Privacy Policy, Terms & Conditions, etc.'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding CMS Pages...')

        pages_data = [
            {
                'title': 'Privacy Policy',
                'slug': 'privacy-policy',
                'icon': 'bi-shield-lock',
                'short_content': 'How we collect, use, and protect your personal information.',
                'content': '<h2>1. Information We Collect</h2><p>We collect information you provide directly to us, such as when you create an account, make a booking, or contact us.</p><h2>2. How We Use Your Information</h2><p>We use the information to process your bookings, communicate with you, and improve our services.</p><h2>3. Data Security</h2><p>We implement appropriate technical and organizational measures to protect your personal data.</p>',
                'meta_title': 'Privacy Policy - Moving Himalaya',
                'meta_description': 'Read our privacy policy to understand how we handle your data.',
                'show_in_menu': False,
                'show_in_footer': True,  
                'is_featured': False,
                'order_level': 10,
                'status': True,
            },
            {
                'title': 'Terms & Conditions',
                'slug': 'terms-and-conditions',
                'icon': 'bi-file-earmark-text',
                'short_content': 'The rules and guidelines for using our services and website.',
                'content': '<h2>1. Acceptance of Terms</h2><p>By accessing and using this website, you accept and agree to be bound by the terms and provision of this agreement.</p><h2>2. Booking and Payment</h2><p>All bookings are subject to availability. A deposit is required to confirm your reservation.</p><h2>3. Cancellation Policy</h2><p>Cancellations made 30 days prior to the trip will receive a full refund minus a small administrative fee.</p>',
                'meta_title': 'Terms & Conditions - Moving Himalaya',
                'meta_description': 'Our terms and conditions for booking travel services.',
                'show_in_menu': False,
                'show_in_footer': True, 
                'is_featured': False,
                'order_level': 11,
                'status': True,
            },
            {
                'title': 'About Us',
                'slug': 'about-us',
                'icon': 'bi-info-circle',
                'short_content': 'Learn about our journey, mission, and the team behind Moving Himalaya.',
                'content': '<p>Moving Himalaya is a premier adventure travel company based in Kathmandu, Nepal. Founded by a group of passionate mountaineers and travel enthusiasts, we are dedicated to providing safe, authentic, and sustainable travel experiences in the Himalayas.</p>',
                'meta_title': 'About Us - Moving Himalaya',
                'meta_description': 'Discover the story and mission behind Moving Himalaya Adventure Travel.',
                'show_in_menu': True,   
                'show_in_footer': True,
                'is_featured': True,
                'order_level': 1,
                'status': True,
            }
        ]

        for page in pages_data:
            Page.objects.update_or_create(
                slug=page['slug'],
                defaults=page
            )

        self.stdout.write(self.style.SUCCESS('✅ CMS Pages (including Privacy & Terms) seeded successfully!'))