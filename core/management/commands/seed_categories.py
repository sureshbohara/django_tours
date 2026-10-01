from django.core.management.base import BaseCommand
from categories.models import Category 

class Command(BaseCommand):
    help = 'Seeds Categories with relevant excerpts (Destinations removed)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Categories...')

        # 1. TREKKING
        trekking, _ = Category.objects.update_or_create(
            slug='trekking', 
            defaults={
                'parent': None, 
                'name': 'Trekking', 
                'excerpt': 'Explore the majestic Himalayas with our curated trekking packages across every region of Nepal.', 
                'font_icon': 'bi-backpack', 
                'order_level': 1, 
                'status': True
            }
        )
        trekking_subs = [
            {'name': 'Annapurna Region', 'slug': 'annapurna-region', 'excerpt': 'Trek through diverse landscapes, from lush subtropical forests to the high-altitude desert of Mustang.', 'order_level': 1},
            {'name': 'Everest Region', 'slug': 'everest-region', 'excerpt': 'Embark on an adventure to the base of the world\'s highest peak and experience unique Sherpa culture.', 'order_level': 2},
            {'name': 'Langtang Region', 'slug': 'langtang-region', 'excerpt': 'Discover the pristine beauty of the Langtang valley, known as the valley of glaciers and Tamang heritage.', 'order_level': 3},
            {'name': 'Manaslu Region', 'slug': 'manaslu-region', 'excerpt': 'Experience the remote trails around the 8th highest mountain and the restricted, mystical Tsum Valley.', 'order_level': 4},
            {'name': 'Dolpa Region', 'slug': 'dolpa-region', 'excerpt': 'Journey into the hidden landscapes of upper Dolpo, a preserved Tibetan culture region beyond the Himalayas.', 'order_level': 5},
            {'name': 'Nepal Western Region', 'slug': 'nepal-western-region', 'excerpt': 'Explore off-the-beaten-path trails in Western Nepal, offering untouched natural beauty and raw adventure.', 'order_level': 6},
            {'name': 'Nepal Eastern Region', 'slug': 'nepal-eastern-region', 'excerpt': 'Trek the rugged and unspoiled terrains of Eastern Nepal, home to the third highest peak, Kanchenjunga.', 'order_level': 7},
            {'name': 'Tibet Tour', 'slug': 'tibet-tour', 'excerpt': 'Combine cultural tours and high-altitude trekking in the mystical land of Tibet and Everest North Face.', 'order_level': 8},
            {'name': 'Great Himalayan Trail', 'slug': 'great-himalayan-trail', 'excerpt': 'The ultimate long-distance trekking route spanning the entire length of the Nepalese Himalayas.', 'order_level': 9},
            {'name': 'Nepal Tour', 'slug': 'nepal-tour', 'excerpt': 'Comprehensive trekking and cultural tours across the diverse landscapes and heritage sites of Nepal.', 'order_level': 10},
        ]
        for sub in trekking_subs:
            Category.objects.update_or_create(
                slug=sub['slug'], 
                defaults={
                    'parent': trekking, 
                    'name': sub['name'], 
                    'excerpt': sub['excerpt'], 
                    'order_level': sub['order_level'], 
                    'status': True
                }
            )

        # 2. EXPEDITIONS
        expeditions, _ = Category.objects.update_or_create(
            slug='expeditions', 
            defaults={
                'parent': None, 
                'name': 'Expeditions', 
                'excerpt': 'Challenge yourself with our extreme high-altitude mountain climbing expeditions led by expert Sherpas.', 
                'font_icon': 'bi-triangle', 
                'order_level': 2, 
                'status': True
            }
        )
        expedition_subs = [
            {'name': '6000m Peaks', 'slug': '6000m-peaks', 'excerpt': 'Climbing expeditions to stunning peaks ranging between 6,000 and 6,999 meters, perfect for advanced trekkers.', 'order_level': 1},
            {'name': '7000m Peaks', 'slug': '7000m-peaks', 'excerpt': 'Extreme high-altitude climbing challenges in the 7,000-meter range for experienced mountaineers.', 'order_level': 2},
            {'name': '8000m Peaks', 'slug': '8000m-peaks', 'excerpt': 'The ultimate mountaineering goal: conquering the mighty 8,000-meter giants of the world with full support.', 'order_level': 3},
        ]
        for sub in expedition_subs:
            Category.objects.update_or_create(
                slug=sub['slug'], 
                defaults={
                    'parent': expeditions, 
                    'name': sub['name'], 
                    'excerpt': sub['excerpt'], 
                    'order_level': sub['order_level'], 
                    'status': True
                }
            )

        # 3. TOURS
        tours, _ = Category.objects.update_or_create(
            slug='tours', 
            defaults={
                'parent': None, 
                'name': 'Tours', 
                'excerpt': 'Cultural, historical, and scenic tours across Nepal and Tibet for a relaxed Himalayan experience.', 
                'font_icon': 'bi-bus-front', 
                'order_level': 3, 
                'status': True
            }
        )
        tour_subs = [
            {'name': 'Cultural Tours', 'slug': 'cultural-tours', 'excerpt': 'Immerse yourself in local traditions, ancient temples, and the living heritage of the Himalayan people.', 'order_level': 1},
            {'name': 'City Tours', 'slug': 'city-tours', 'excerpt': 'Explore the vibrant cities, bustling markets, and UNESCO historical landmarks of Kathmandu Valley.', 'order_level': 2},
            {'name': 'Wildlife Safari', 'slug': 'wildlife-safari', 'excerpt': 'Discover diverse wildlife including one-horned rhinos, royal Bengal tigers, and elephants in national parks.', 'order_level': 3},
        ]
        for sub in tour_subs:
            Category.objects.update_or_create(
                slug=sub['slug'], 
                defaults={
                    'parent': tours, 
                    'name': sub['name'], 
                    'excerpt': sub['excerpt'], 
                    'order_level': sub['order_level'], 
                    'status': True
                }
            )

        # 4. EXPERIENCES
        experiences, _ = Category.objects.update_or_create(
            slug='experiences', 
            defaults={
                'parent': None, 
                'name': 'Experiences', 
                'excerpt': 'Unique, hands-on activities hosted by local experts to make your trip truly memorable.', 
                'font_icon': 'bi-stars', 
                'order_level': 4, 
                'status': True
            }
        )
        exp_subs = [
            {'name': 'Adventure Activities', 'slug': 'adventure-activities', 'excerpt': 'Paragliding, bungee jumping, white-water rafting, and mountain biking for ultimate thrill-seekers.', 'order_level': 1},
            {'name': 'Wellness & Yoga', 'slug': 'wellness-yoga', 'excerpt': 'Rejuvenate your mind and body with yoga retreats and meditation sessions in the peaceful Himalayas.', 'order_level': 2},
        ]
        for sub in exp_subs:
            Category.objects.update_or_create(
                slug=sub['slug'], 
                defaults={
                    'parent': experiences, 
                    'name': sub['name'], 
                    'excerpt': sub['excerpt'], 
                    'order_level': sub['order_level'], 
                    'status': True
                }
            )

        # 5. SERVICES
        services, _ = Category.objects.update_or_create(
            slug='services', 
            defaults={
                'parent': None, 
                'name': 'Services', 
                'excerpt': 'Essential travel support to make your Himalayan journey seamless, safe, and hassle-free.', 
                'font_icon': 'bi-briefcase', 
                'order_level': 5, 
                'status': True
            }
        )
        serv_subs = [
            {'name': 'Airport Transfers', 'slug': 'airport-transfers', 'excerpt': 'Reliable 24/7 airport pickup, drop-off, and private vehicle hire services for your comfort.', 'order_level': 1},
            {'name': 'Visa Assistance', 'slug': 'visa-assistance', 'excerpt': 'Hassle-free Nepal visa, TIMS, and restricted area permit processing support by our experts.', 'order_level': 2},
            {'name': 'Guide & Porter Booking', 'slug': 'guide-porter-booking', 'excerpt': 'Certified, experienced, and English-speaking guides and porters to ensure your safety on trails.', 'order_level': 3},
        ]
        for sub in serv_subs:
            Category.objects.update_or_create(
                slug=sub['slug'], 
                defaults={
                    'parent': services, 
                    'name': sub['name'], 
                    'excerpt': sub['excerpt'], 
                    'order_level': sub['order_level'], 
                    'status': True
                }
            )

        self.stdout.write(self.style.SUCCESS('✅ Categories seeded successfully with relevant excerpts!'))