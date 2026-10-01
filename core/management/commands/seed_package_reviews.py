from django.core.management.base import BaseCommand
from packages.models import Package
from package_reviews.models import PackageReview

class Command(BaseCommand):
    help = 'Seeds the PackageReview table with realistic default reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Package Reviews...')

     
        reviews_data = [
            {
                'name': 'Suresh Bohara',
                'email': 'suresh.bohara@example.com',
                'rating': 5,
                'comment': 'An absolutely life-changing experience. The guides were professional, the food was surprisingly good, and the views from Kala Patthar were beyond words! Highly recommended.',
                'status': True
            },
            {
                'name': 'Sarah Jenkins',
                'email': 'sarah.jenkins@example.com',
                'rating': 5,
                'comment': 'The Everest Base Camp trek was the highlight of my life. Our guide Pasang was incredibly knowledgeable and made sure we were safe and comfortable at every step. The tea houses were cozy and the food was delicious.',
                'status': True
            },
            {
                'name': 'Michael Chen',
                'email': 'michael.chen@example.com',
                'rating': 4,
                'comment': 'Great trek with breathtaking views. The altitude was challenging but the acclimatization days helped a lot. Only minor issue was the Wi-Fi was spotty in higher altitudes, but that is expected in the mountains.',
                'status': True
            },
            {
                'name': 'Emma Watson',
                'email': 'emma.watson@example.com',
                'rating': 5,
                'comment': 'Moving Himalaya Adventure Travel did a fantastic job organizing everything. From the flights to Lukla to the permits, everything was seamless. I will definitely book another trek with them!',
                'status': True
            },
            {
                'name': 'Rajesh Kumar',
                'email': 'rajesh.kumar@example.com',
                'rating': 5,
                'comment': 'Namche Bazaar and Tengboche Monastery were mesmerizing. The porters and guides were very friendly and supportive. A must-do trek for any adventure lover visiting Nepal.',
                'status': True
            },
            {
                'name': 'Julia Roberts',
                'email': 'julia.roberts@example.com',
                'rating': 4,
                'comment': 'Beautiful scenery and well-managed itinerary. The teahouses were basic but comfortable. Make sure to bring a good sleeping bag and down jacket as it gets very cold at night above Dingboche.',
                'status': True
            },
            {
                'name': 'David Smith',
                'email': 'david.smith@example.com',
                'rating': 5,
                'comment': 'Reaching Everest Base Camp was a dream come true. The team was extremely supportive, especially when I felt a bit of altitude sickness. They knew exactly what to do. Thank you team!',
                'status': True
            },
            {
                'name': 'Aiko Tanaka',
                'email': 'aiko.tanaka@example.com',
                'rating': 5,
                'comment': 'Perfectly organized trip. The balance between trekking and acclimatization was just right. The cultural experience in the Khumbu region was as memorable as the mountains themselves.',
                'status': True
            },
            {
                'name': 'Carlos Mendez',
                'email': 'carlos.mendez@example.com',
                'rating': 4,
                'comment': 'Excellent trekking experience. The flight to Lukla was thrilling! The guides were very experienced and kept a steady pace. Highly recommend this agency for solo travelers.',
                'status': True
            },
            {
                'name': 'Priya Sharma',
                'email': 'priya.sharma@example.com',
                'rating': 5,
                'comment': 'I traveled with my family and everyone had a wonderful time. The staff took great care of us, even adjusting the menu for vegetarian options. Five stars from our family!',
                'status': True
            }
        ]

       
        packages = list(Package.objects.filter(status=True))
        if not packages:
            self.stdout.write(self.style.ERROR('❌ No packages found. Run "python manage.py seed_packages" first.'))
            return

        created_count = 0
        
  
        for i, review_data in enumerate(reviews_data):
            package = packages[i % len(packages)]
            
            PackageReview.objects.update_or_create(
                email=review_data['email'],
                package=package,
                defaults={
                    'name': review_data['name'],
                    'rating': review_data['rating'],
                    'comment': review_data['comment'],
                    'status': review_data['status']
                }
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Successfully seeded {created_count} realistic package reviews!'))