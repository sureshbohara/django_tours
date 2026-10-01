from django.core.management.base import BaseCommand
from faqs.models import Faq  

class Command(BaseCommand):
    help = 'Seeds the FAQ table with default questions and answers'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding FAQs...')

        faqs_data = [
            {'display_on': 'account', 'question': 'How do I create an account on Ghum Nepal Portal?', 'answer': 'To create an account, click on the "Register" button located at the top right corner of our homepage. Fill in your name, email address, and password, then click "Sign Up".', 'order_level': 1, 'status': True},
            {'display_on': 'account', 'question': 'Can I sign up using Google, Facebook, or Apple ID?', 'answer': 'Yes, Ghum Nepal Portal supports social login. On the login or registration page, click the "Login with Google" or "Login with Facebook" button.', 'order_level': 2, 'status': True},
            {'display_on': 'account', 'question': 'Do I need an account to book a hotel?', 'answer': 'While you can browse properties without an account, you must create and log into an account to complete a booking.', 'order_level': 3, 'status': True},
            {'display_on': 'account', 'question': 'What should I do if I forget my password?', 'answer': 'If you forget your password, click on the "Login" button, then select "Forgot Password". Enter your registered email address.', 'order_level': 4, 'status': True},
            {'display_on': 'account', 'question': 'Can I change my email address after signing up?', 'answer': 'Currently, for security reasons, you cannot change your primary email address directly. Please contact customer support.', 'order_level': 5, 'status': True},
            {'display_on': 'account', 'question': 'Why am I unable to log in to my account?', 'answer': 'Ensure you are using the correct email and password. Check if Caps Lock is on. Try resetting your password.', 'order_level': 6, 'status': True},
            {'display_on': 'account', 'question': 'How do I update my profile information?', 'answer': 'Log in to your account, go to your Dashboard, and click on the "Settings" tab to update your details.', 'order_level': 7, 'status': True},
            {'display_on': 'account', 'question': 'Can I delete my account permanently?', 'answer': 'Yes, you can request account deletion. Please contact our customer support team for assistance.', 'order_level': 8, 'status': True},
            {'display_on': 'account', 'question': 'Why do I need to verify my email address?', 'answer': 'Email verification ensures the security of your account and confirms the email belongs to you.', 'order_level': 9, 'status': True},
            {'display_on': 'account', 'question': 'How do I verify my email?', 'answer': 'After signing up, a verification link is sent to your email inbox. Click the "Verify Email Address" button.', 'order_level': 10, 'status': True},
        ]

        for faq in faqs_data:
            Faq.objects.update_or_create(
                question=faq['question'],
                defaults=faq
            )

        self.stdout.write(self.style.SUCCESS('✅ FAQs seeded successfully!'))