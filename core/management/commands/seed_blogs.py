from django.core.management.base import BaseCommand
from blogs.models import Post    
from categories.models import Category 

class Command(BaseCommand):
    help = 'Seeds the Post (Blog) table with realistic travel articles'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Blog Posts...')

        blog_category = Category.objects.filter(slug='travel-blog').first()
        if not blog_category:
            blog_category, _ = Category.objects.get_or_create(
                slug='travel-blog',
                defaults={'name': 'Travel Blog', 'status': True, 'order_level': 99}
            )

        # 2. Blog Posts Data
        posts_data = [
            {
                'category': blog_category,
                'title': 'Top 10 Tips for Trekking in the Himalayas',
                'slug': 'top-10-tips-trekking-himalayas',
                'excerpt': 'Essential advice for first-time trekkers planning an adventure in the majestic Himalayas of Nepal.',
                'description': '<h2>1. Start Training Early</h2><p>Physical preparation is key. Start cardio and strength training at least 2 months before your trip.</p><h2>2. Pack Light but Smart</h2><p>Focus on layered clothing. A good down jacket and waterproof shell are mandatory.</p><h2>3. Stay Hydrated</h2><p>Drink at least 3-4 liters of water daily to help your body acclimatize to the altitude.</p>',
                'meta_title': 'Top 10 Trekking Tips for the Himalayas | Moving Himalaya',
                'meta_description': 'Discover the top 10 essential tips for a safe and enjoyable trekking experience in the Himalayas.',
                'views': 1250,
                'is_featured': True,
                'status': True,
                'order_level': 1,
            },
            {
                'category': blog_category,
                'title': 'Best Time to Visit Nepal: A Complete Seasonal Guide',
                'slug': 'best-time-to-visit-nepal-seasonal-guide',
                'excerpt': 'Discover the ideal months to plan your Nepal adventure, from clear mountain views to vibrant festivals.',
                'description': '<p>Nepal is a year-round destination, but the best times to visit are undoubtedly <strong>Spring (March to May)</strong> and <strong>Autumn (September to November)</strong>.</p><p>During these seasons, the weather is stable, the skies are clear, and the temperatures are moderate, offering the best views of the Himalayan peaks.</p>',
                'meta_title': 'Best Time to Visit Nepal | Seasonal Travel Guide',
                'meta_description': 'Plan your trip perfectly with our comprehensive guide on the best seasons to visit Nepal for trekking and tours.',
                'views': 890,
                'is_featured': False,
                'status': True,
                'order_level': 2,
            },
            {
                'category': blog_category,
                'title': 'What to Pack for the Everest Base Camp Trek',
                'slug': 'what-to-pack-everest-base-camp-trek',
                'excerpt': 'A comprehensive packing list to ensure you have everything you need for a successful EBC adventure.',
                'description': '<h2>Clothing Layers</h2><ul><li>Moisture-wicking base layers</li><li>Insulating mid-layers (fleece/down)</li><li>Waterproof and windproof outer shell</li></ul><h2>Essential Gear</h2><ul><li>Broken-in trekking boots</li><li>Sleeping bag (rated to -15°C)</li><li>Trekking poles</li><li>Headlamp with extra batteries</li></ul>',
                'meta_title': 'Everest Base Camp Packing List | Moving Himalaya',
                'meta_description': 'Download our ultimate packing checklist for the Everest Base Camp trek to ensure you are fully prepared.',
                'views': 2100,
                'is_featured': True,
                'status': True,
                'order_level': 3,
            },
            {
                'category': blog_category,
                'title': 'Understanding Altitude Sickness: A Guide for Trekkers',
                'slug': 'understanding-altitude-sickness-guide',
                'excerpt': 'Learn how to recognize, prevent, and manage Acute Mountain Sickness (AMS) during your high-altitude trek.',
                'description': '<p>Acute Mountain Sickness (AMS) is a real concern above 2,500 meters. The golden rule is: <strong>"Climb high, sleep low."</strong></p><p>Listen to your body. If you experience a persistent headache, nausea, or dizziness, do not ascend further. Inform your guide immediately and be prepared to descend if symptoms worsen.</p>',
                'meta_title': 'Altitude Sickness Guide for Trekkers in Nepal',
                'meta_description': 'Stay safe on the trails. Learn the symptoms, prevention, and treatment of altitude sickness in Nepal.',
                'views': 1540,
                'is_featured': False,
                'status': True,
                'order_level': 4,
            },
            {
                'category': blog_category,
                'title': 'Cultural Etiquette: Respecting Local Traditions in Nepal',
                'slug': 'cultural-etiquette-respecting-local-traditions-nepal',
                'excerpt': 'A brief guide to understanding and respecting the rich cultural and religious traditions of the Nepali people.',
                'description': '<p>Nepal is a deeply spiritual country. When visiting monasteries or temples, always walk clockwise around stupas.</p><p>Always ask for permission before photographing locals, especially in rural villages. Remove your shoes before entering someone\'s home or a religious site, and never point your feet at people or religious altars.</p>',
                'meta_title': 'Cultural Etiquette and Traditions in Nepal',
                'meta_description': 'Travel responsibly. Learn about Nepali cultural etiquette, customs, and how to show respect during your visit.',
                'views': 670,
                'is_featured': False,
                'status': True,
                'order_level': 5,
            }
        ]

        # 3. Loop Through and Create/Update
        for post_data in posts_data:
            post_data['image'] = None 
            
            post, created = Post.objects.update_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            
            action = "Created" if created else "Updated"
            self.stdout.write(f"  ✅ {action}: {post_data['title']}")

        self.stdout.write(self.style.SUCCESS('🚀 Blog Posts seeded successfully!'))