from django.core.management.base import BaseCommand
from datetime import date, timedelta
from promos.models import PromoCode 

class Command(BaseCommand):
    help = 'Seeds the PromoCode table with default discount codes'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Promo Codes...')

        promos_data = [
            {
                'code': 'WELCOME10',
                'discount_type': 'percentage',
                'discount_value': 10.00,
                'min_amount': 0.00,
                'max_uses': 100,
                'used_count': 0,
                'expires_at': date.today() + timedelta(days=365),
                'status': True,
            },
            {
                'code': 'SUMMER50',
                'discount_type': 'fixed',
                'discount_value': 50.00,
                'min_amount': 500.00,
                'max_uses': 50,
                'used_count': 0,
                'expires_at': date.today() + timedelta(days=90),
                'status': True,
            },
            {
                'code': 'EARLYBIRD',
                'discount_type': 'percentage',
                'discount_value': 15.00,
                'min_amount': 1000.00,
                'max_uses': 0, 
                'used_count': 0,
                'expires_at': date.today() + timedelta(days=30),
                'status': True,
            }
        ]

        for promo in promos_data:
            PromoCode.objects.update_or_create(
                code=promo['code'],
                defaults=promo
            )

        self.stdout.write(self.style.SUCCESS('✅ Promo Codes seeded successfully!'))