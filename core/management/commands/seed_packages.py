from django.core.management.base import BaseCommand
from packages.models import Package
from categories.models import Category

class Command(BaseCommand):
    help = 'Seeds Packages mapped to specific Categories (Deduplicated)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Packages...')

        # 1. Categories Fetch गर्ने
        cats = {
            'annapurna': Category.objects.filter(slug='annapurna-region').first(),
            'everest': Category.objects.filter(slug='everest-region').first(),
            'langtang': Category.objects.filter(slug='langtang-region').first(),
            'manaslu': Category.objects.filter(slug='manaslu-region').first(),
            '6000m': Category.objects.filter(slug='6000m-peaks').first(),
            '7000m': Category.objects.filter(slug='7000m-peaks').first(),
            '8000m': Category.objects.filter(slug='8000m-peaks').first(),
        }

        # 2. Default Template 
        default_template = {
            'status': True, 'display_on': 'default',
            'included_data': [{"content": "Airport Transfers"}, {"content": "Experienced Guide"}, {"content": "All Meals"}],
            'excluded_data': [{"content": "International Flights"}, {"content": "Travel Insurance"}, {"content": "Personal Expenses"}],
            'itinerary_data': [
                {"name": "Arrival in Kathmandu", "content": "Welcome to Nepal. Transfer to hotel.", "max_elevation": "1400m", "duration": "1 hr", "distance": "6 km", "meals": "Dinner", "accommodation": "Hotel"},
                {"name": "Preparation and Sightseeing", "content": "City tour and trip briefing.", "max_elevation": "1400m", "duration": "5 hrs", "distance": "10 km", "meals": "Breakfast, Lunch, Dinner", "accommodation": "Hotel"}
            ],
            'general': [{"content": "T-shirt"}, {"content": "Fleece jacket"}],
            'lower_body': [{"content": "Trekking pants"}, {"content": "Woolen socks"}],
            'upper_body': [{"content": "Down jacket"}, {"content": "Windproof jacket"}],
            'footwear': [{"content": "Trekking boots"}, {"content": "Camp shoes"}],
            'accessories': [{"content": "Sunglasses"}, {"content": "Headlamp"}, {"content": "Water bottle"}]
        }

        # 3. Package Data List 
        packages_data = [
            # --- ANNAPURNA REGION ---
            {'name': 'Kang La and Mesokanto La Pass Trek', 'slug': 'kang-la-mesokanto-la-pass-trek', 'cat': 'annapurna', 'price': 1200, 'days': '14 Days'},
            {'name': 'Khopra Ridge Trek', 'slug': 'khopra-ridge-trek', 'cat': 'annapurna', 'price': 900, 'days': '10 Days'},
            {'name': 'Annapurna Circuit and Poon Hill Trek', 'slug': 'annapurna-circuit-poon-hill-trek', 'cat': 'annapurna', 'price': 1300, 'days': '16 Days'},
            {'name': 'Annapurna Circuit Trek', 'slug': 'annapurna-circuit-trek', 'cat': 'annapurna', 'price': 1250, 'days': '18 Days'},
            {'name': 'Narphu Valley Trek', 'slug': 'narphu-valley-trek', 'cat': 'annapurna', 'price': 1500, 'days': '15 Days'},
            {'name': 'Annapurna Base Camp Trek', 'slug': 'annapurna-base-camp-trek', 'cat': 'annapurna', 'price': 950, 'days': '11 Days'},
            {'name': 'Ghorepani Poon Hill Trek', 'slug': 'ghorepani-poon-hill-trek', 'cat': 'annapurna', 'price': 500, 'days': '5 Days'},
            {'name': 'Upper Mustang Trek', 'slug': 'upper-mustang-trek', 'cat': 'annapurna', 'price': 2100, 'days': '14 Days'},

            # --- EVEREST REGION ---
            {'name': 'Everest Three Pass Trek', 'slug': 'everest-three-pass-trek', 'cat': 'everest', 'price': 1600, 'days': '19 Days'},
            {'name': 'Gokyo Ri, Cho La Pass & Everest Base Camp Trek', 'slug': 'gokyo-ri-cho-la-pass-ebc-trek', 'cat': 'everest', 'price': 1650, 'days': '18 Days'},
            {'name': 'Everest Base Camp Trek', 'slug': 'everest-base-camp-trek', 'cat': 'everest', 'price': 1450, 'days': '14 Days'},
            {'name': 'Rolwaling Valley to Everest Trek via Tashi Laptsa Pass', 'slug': 'rolwaling-valley-everest-tashi-laptsa', 'cat': 'everest', 'price': 1800, 'days': '21 Days'},
            {'name': 'Pikey Peak Trek', 'slug': 'pikey-peak-trek', 'cat': 'everest', 'price': 600, 'days': '7 Days'},
            {'name': 'Everest Panorama Trek', 'slug': 'everest-panorama-trek', 'cat': 'everest', 'price': 1100, 'days': '14 Days'},

            # --- LANGTANG REGION ---
            {'name': 'Langtang Valley and Gosaikunda Trek', 'slug': 'langtang-valley-gosaikunda-trek', 'cat': 'langtang', 'price': 950, 'days': '12 Days'},
            {'name': 'Tamang Heritage and Langtang Valley Trek', 'slug': 'tamang-heritage-langtang-valley-trek', 'cat': 'langtang', 'price': 1000, 'days': '14 Days'},
            {'name': 'Langtang Valley Trek', 'slug': 'langtang-valley-trek', 'cat': 'langtang', 'price': 800, 'days': '10 Days'},
            {'name': 'Yoga Retreat Langtang Valley Trek', 'slug': 'yoga-retreat-langtang-valley-trek', 'cat': 'langtang', 'price': 1100, 'days': '12 Days'},
            {'name': 'Tilman Pass Trek via Langtang Valley', 'slug': 'tilman-pass-trek-langtang-valley', 'cat': 'langtang', 'price': 1400, 'days': '18 Days'},
            {'name': 'Paldor Peak Climbing 5,896m', 'slug': 'paldor-peak-climbing-ganesh-himal', 'cat': 'langtang', 'price': 1300, 'days': '15 Days'},
            {'name': 'Ganesh Himal Ruby Valley Trek', 'slug': 'ganesh-himal-ruby-valley-trek', 'cat': 'langtang', 'price': 1200, 'days': '16 Days'},
            {'name': 'Yala Peak Climb with Langtang Trek', 'slug': 'yala-peak-climb-langtang-trek', 'cat': 'langtang', 'price': 1250, 'days': '14 Days'},

            # --- MANASLU REGION ---
            {'name': 'Lower Manaslu, Balcony of Buddha and Ganesh Himal', 'slug': 'lower-manaslu-balcony-buddha-ganesh', 'cat': 'manaslu', 'price': 1400, 'days': '16 Days'},
            {'name': 'Manaslu Trek and Serang Gumba', 'slug': 'manaslu-trek-serang-gumba', 'cat': 'manaslu', 'price': 1350, 'days': '15 Days'},
            {'name': 'Manaslu and Annapurna Trek', 'slug': 'manaslu-annapurna-trek', 'cat': 'manaslu', 'price': 1800, 'days': '22 Days'},
            {'name': 'Rupina La Pass Trek', 'slug': 'rupina-la-pass-trek', 'cat': 'manaslu', 'price': 1500, 'days': '18 Days'},
            {'name': 'Tsum Valley Trek', 'slug': 'tsum-valley-trek', 'cat': 'manaslu', 'price': 1400, 'days': '16 Days'},
            {'name': 'Manaslu Trek via Laprak', 'slug': 'manaslu-trek-via-laprak', 'cat': 'manaslu', 'price': 1300, 'days': '15 Days'},
            {'name': 'Manaslu Circuit Trek', 'slug': 'manaslu-circuit-trek', 'cat': 'manaslu', 'price': 1450, 'days': '16 Days'},
            {'name': 'Manaslu Circuit and Tsum Valley Trek', 'slug': 'manaslu-circuit-tsum-valley-trek', 'cat': 'manaslu', 'price': 1700, 'days': '21 Days'},

            # --- 6000m PEAKS ---
            {'name': 'Lobuche Peak Climbing 6119m', 'slug': 'lobuche-peak-climbing-6119m', 'cat': '6000m', 'price': 1900, 'days': '17 Days'},
            {'name': 'Ama Dablam Expedition 6812m', 'slug': 'ama-dablam-expedition-6812m', 'cat': '6000m', 'price': 3500, 'days': '28 Days'},
            {'name': 'Kyajo Ri Peak Climbing 6186m', 'slug': 'kyajo-ri-peak-climbing-6186m', 'cat': '6000m', 'price': 2100, 'days': '19 Days'},
            {'name': 'Dhampus (Thapa) Peak Climbing 6,012m', 'slug': 'dhampus-thapa-peak-climbing-6012m', 'cat': '6000m', 'price': 1800, 'days': '16 Days'},
            {'name': 'Mera Peak Climbing 6476m', 'slug': 'mera-peak-climbing-6476m', 'cat': '6000m', 'price': 2000, 'days': '19 Days'},
            {'name': 'Chulu East Peak Climbing 6,584m', 'slug': 'chulu-east-peak-climbing-6584m', 'cat': '6000m', 'price': 2200, 'days': '20 Days'},
            {'name': 'Larkya Peak Climbing 6,416m', 'slug': 'larkya-peak-climbing-6416m', 'cat': '6000m', 'price': 2100, 'days': '19 Days'},
            {'name': 'Island Peak and Three High Pass', 'slug': 'island-peak-three-high-pass', 'cat': '6000m', 'price': 2300, 'days': '22 Days'},

            # --- 7000m PEAKS ---
            {'name': 'Himlung Himal Expedition', 'slug': 'himlung-himal-expedition', 'cat': '7000m', 'price': 4500, 'days': '30 Days'},
            {'name': 'Putha Hiunchuli Expedition', 'slug': 'putha-hiunchuli-expedition', 'cat': '7000m', 'price': 4200, 'days': '28 Days'},
            {'name': 'Saipal Himal Expedition', 'slug': 'saipal-himal-expedition', 'cat': '7000m', 'price': 4800, 'days': '32 Days'},
            {'name': 'Mount Gyajikang Expedition', 'slug': 'mount-gyajikang-expedition', 'cat': '7000m', 'price': 5000, 'days': '35 Days'},
            {'name': 'Baruntse Expedition', 'slug': 'baruntse-expedition', 'cat': '7000m', 'price': 5500, 'days': '35 Days'},
            {'name': 'Annapurna IV Expedition (7,525 m)', 'slug': 'annapurna-iv-expedition-7525m', 'cat': '7000m', 'price': 6000, 'days': '35 Days'},
            {'name': 'Gangapurna Expedition (7,455 m)', 'slug': 'gangapurna-expedition-7455m', 'cat': '7000m', 'price': 5800, 'days': '35 Days'},
            {'name': 'Churen Himal Expedition (7,371 m)', 'slug': 'churen-himal-expedition-7371m', 'cat': '7000m', 'price': 5500, 'days': '35 Days'},

            # --- 8000m PEAKS ---
            {'name': 'Makalu Expedition (8485m)', 'slug': 'makalu-expedition-8485m', 'cat': '8000m', 'price': 12000, 'days': '50 Days'},
            {'name': 'Annapurna 1 Expedition (8091m)', 'slug': 'annapurna-1-expedition-8091m', 'cat': '8000m', 'price': 13000, 'days': '50 Days'},
            {'name': 'Kanchenjunga Expedition (8586m)', 'slug': 'kanchenjunga-expedition-8586m', 'cat': '8000m', 'price': 14000, 'days': '55 Days'},
            {'name': 'Manaslu Expedition (8163m)', 'slug': 'manaslu-expedition-8163m', 'cat': '8000m', 'price': 11000, 'days': '45 Days'},
            {'name': 'Everest Climbing Expedition (8848m) South Route', 'slug': 'everest-climbing-expedition-8848m-south', 'cat': '8000m', 'price': 45000, 'days': '60 Days'},
            {'name': 'Dhaulagiri Expedition (8167m)', 'slug': 'dhaulagiri-expedition-8167m', 'cat': '8000m', 'price': 12500, 'days': '45 Days'},
            {'name': 'Lhotse Expedition (8516m)', 'slug': 'lhotse-expedition-8516m', 'cat': '8000m', 'price': 15000, 'days': '50 Days'},
        ]

        # 4. Loop Through and Create/Update
        for pkg in packages_data:
            category_obj = cats.get(pkg['cat'])
            
         
            pkg_data = default_template.copy()
            pkg_data.update({
                'name': pkg['name'],
                'slug': pkg['slug'],
                'trip_price': pkg['price'],
                'duration': pkg['days'],
                'excerpt': f"Experience the ultimate adventure with {pkg['name']}.",
                'description': f"This {pkg['days']} journey takes you through the heart of the Himalayas.",
            })

            package, created = Package.objects.update_or_create(
                slug=pkg['slug'],
                defaults=pkg_data
            )

            # ManyToMany Category Assign 
            if category_obj:
                package.categories.set([category_obj])
            
            self.stdout.write(f"  ✅ {'Created' if created else 'Updated'}: {pkg['name']}")

        self.stdout.write(self.style.SUCCESS(f'🚀 Successfully seeded {len(packages_data)} packages!'))