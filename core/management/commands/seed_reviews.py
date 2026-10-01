from django.core.management.base import BaseCommand
from reviews.models import Review 

class Command(BaseCommand):
    help = 'Seeds the Review table with default customer testimonials'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Reviews...')

        reviews_data = [
            {
                'name': 'John Doe',
                'email': 'john.doe@example.com',
                'address': 'New York, USA',
                'rating': 5,
                'review': 'An absolutely breathtaking experience! The guides were incredibly knowledgeable, and the views of the Himalayas were out of this world. Highly recommended for anyone looking for an adventure.',
                'content': 'The Everest Base Camp trek was a dream come true. The team took care of everything, from permits to meals. I felt safe and supported throughout the journey.',
                'display_on': 'home',
                'order_level': 1,
                'status': True,
            },
            {
                'name': 'Sarah Smith',
                'email': 'sarah.smith@example.com',
                'address': 'London, UK',
                'rating': 5,
                'review': 'Moving Himalaya provided the best cultural tour experience. The local homestays were authentic, and the food was delicious. A truly immersive journey!',
                'content': 'We loved the Village Homestay package. It gave us a real glimpse into the daily life of Nepali people. The hospitality was warm and unforgettable.',
                'display_on': 'home',
                'order_level': 2,
                'status': True,
            },
            {
                'name': 'Michael Chen',
                'email': 'm.chen@example.com',
                'address': 'Toronto, Canada',
                'rating': 4,
                'review': 'Great organization and smooth logistics. The Annapurna Circuit was challenging but rewarding. The porters were very helpful and friendly.',
                'content': 'The only minor issue was the weather, but that is beyond anyone\'s control. The team adjusted our itinerary perfectly to ensure we got the best mountain views.',
                'display_on': 'default',
                'order_level': 3,
                'status': True,
            },
            {
                'name': 'Emma Wilson',
                'email': 'emma.w@example.com',
                'address': 'Sydney, Australia',
                'rating': 5,
                'review': 'I booked the Wildlife Safari in Chitwan and it was fantastic! Saw rhinos, elephants, and even a tiger from a distance. The naturalist guide was excellent.',
                'content': 'Everything was well-planned. The jungle lodge was comfortable and the canoe ride was a highlight. Will definitely book another tour with them.',
                'display_on': 'default',
                'order_level': 4,
                'status': True,
            },
            {
                'name': 'David Miller',
                'email': 'david.m@example.com',
                'address': 'Berlin, Germany',
                'rating': 5,
                'review': 'Professional, reliable, and friendly. They made our honeymoon in Nepal very special. The mountain flight and resort in Pokhara were perfect.',
                'content': 'Thank you for making our trip so memorable. The attention to detail and the surprise arrangements were much appreciated.',
                'display_on': 'home',
                'order_level': 5,
                'status': True,
            },
   
            {
                'name': 'Liam O\'Connor',
                'email': 'liam.oconnor@example.com',
                'address': 'Dublin, Ireland',
                'rating': 5,
                'review': 'The Upper Mustang trek was a surreal experience. The ancient caves, desert-like landscape, and rich Tibetan culture made it the highlight of my travels in Asia.',
                'content': 'Moving Himalaya handled the restricted area permits flawlessly. Our guide was not only knowledgeable about the history of the region but also incredibly attentive to our pace and health. The teahouses were comfortable, and the food was surprisingly good for such a remote area.',
                'display_on': 'home',
                'order_level': 6,
                'status': True,
            },
        ]

        for review in reviews_data:

            Review.objects.update_or_create(
                email=review['email'],
                defaults=review
            )

        self.stdout.write(self.style.SUCCESS('✅ Reviews seeded successfully!'))