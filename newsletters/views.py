from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mass_mail
from django.conf import settings
from .models import Subscriber
from .forms import NewsletterForm

@login_required
def subscriber_list(request):
    subscribers = Subscriber.objects.all()
    search = request.GET.get('search')
    if search:
        subscribers = subscribers.filter(email__icontains=search)
    return render(request, 'admin/newsletters/index.html', {'items': subscribers, 'filters': request.GET})

@login_required
def subscriber_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Subscriber, pk=pk).delete()
        return JsonResponse({'success': True, 'message': 'Subscriber deleted!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def send_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            

            subscribers = Subscriber.objects.filter(is_active=True)
            email_list = [sub.email for sub in subscribers]
            
            if not email_list:
                return JsonResponse({'success': False, 'message': 'No active subscribers found!'}, status=400)


            email_tuples = [
                (subject, message, settings.DEFAULT_FROM_EMAIL, [email]) 
                for email in email_list
            ]
            
            try:

                send_mass_mail(email_tuples, fail_silently=False)
                return JsonResponse({'success': True, 'message': f'Newsletter sent to {len(email_list)} subscribers successfully!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Failed to send emails: {str(e)}'}, status=500)
                
    else:
        form = NewsletterForm()
        
    return render(request, 'admin/newsletters/send_form.html', {'form': form})