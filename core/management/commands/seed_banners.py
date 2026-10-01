from django.core.management.base import BaseCommand
from banners.models import Banner

class Command(BaseCommand):
    help = 'Seeds the Banner table with 3 default hero banners'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Banners...')

        banners_data = [
            {
                'title': 'Trekking in Nepal, Land of the Himalayas',
                'subtitle': 'Thrilling, inspiring trekking routes and mountaineering packages across every region of Nepal.',
                'description': 'Join us for an unforgettable journey through the majestic mountains with expert local guides.',
                'order_level': 1,
                'status': True,
                'image': None 
            },
            {
                'title': 'Summit the World\'s Highest Peaks',
                'subtitle': 'From Everest Base Camp to Island Peak, join professional climbing expeditions for every skill level.',
                'description': 'Expert guides, top-tier equipment, and ultimate safety for your high-altitude climbing adventure.',
                'order_level': 2,
                'status': True,
            },
            {
                'title': 'Discover the Rich Culture of the Himalayas',
                'subtitle': 'Experience authentic village life, ancient monasteries, and vibrant festivals on our guided cultural tours.',
                'description': 'Immerse yourself in the rich traditions, warm hospitality, and breathtaking landscapes of Nepal.',
                'order_level': 3,
                'status': True,
            }
        ]

        for banner_data in banners_data:
            Banner.objects.update_or_create(
                title=banner_data['title'],
                defaults=banner_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {banner_data['title']}")

        self.stdout.write(self.style.SUCCESS('✅ 3 Banners seeded successfully!'))