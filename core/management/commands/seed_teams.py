from django.core.management.base import BaseCommand
from teams.models import Team  # App को नाम 'teams' वा 'team' भए अनुसार सच्याउनुहोला

class Command(BaseCommand):
    help = 'Seeds the Team table with default staff members'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Team Members...')

        teams_data = [
            {
                'name': 'Tenzing Sherpa',
                'role': 'guide',
                'email': 'tenzing@movinghimalaya.com',
                'phone': '+977 9800000001',
                'address': 'Thamel, Kathmandu',
                'bio': 'Certified mountain guide with over 15 years of experience in Everest and Annapurna regions.',
                'image': None, 
                'facebook': 'https://facebook.com/tenzing',
                'order_level': 1,
                'status': True,
            },
            {
                'name': 'Sita Tamang',
                'role': 'office',
                'email': 'sita@movinghimalaya.com',
                'phone': '+977 9800000002',
                'address': 'Nagarjun, Kathmandu',
                'bio': 'Our friendly tour consultant ensuring your trip is perfectly planned from start to finish.',
                'image': None, 
                'instagram': 'https://instagram.com/sita',
                'order_level': 2,
                'status': True,
            },
            {
                'name': 'Ram Bahadur',
                'role': 'porter',
                'email': 'ram@movinghimalaya.com',
                'phone': '+977 9800000003',
                'address': 'Solukhumbu, Nepal',
                'bio': 'Strong, reliable, and experienced high-altitude porter dedicated to your safety and comfort.',
                'image': None, 
                'order_level': 3,
                'status': True,
            }
        ]

        for member in teams_data:
            Team.objects.update_or_create(
                name=member['name'],
                defaults=member
            )

        self.stdout.write(self.style.SUCCESS('✅ Team Members seeded successfully!'))