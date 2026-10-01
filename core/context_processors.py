from settings.models import SiteSetting
from categories.models import Category
from pages.models import Page
from teams.models import Team 
def global_settings(request):
    setting = SiteSetting.get_instance() 

    footer_categories = Category.objects.filter(
        parent__isnull=True, 
        status=True
    ).prefetch_related('children').order_by('order_level')[:4]
    
    footer_pages = Page.objects.filter(status=True).order_by('order_level')[:4]

    footer_experts = Team.objects.filter(status=True).order_by('order_level')[:4]

    trekking_regions = Category.objects.filter(parent__slug='trekking', status=True).order_by('order_level')[:4]
    
    return {
        'setting': setting,
        'global_categories': footer_categories,
        'global_pages': footer_pages,
        'footer_experts': footer_experts,
        'trekking_regions': trekking_regions,
    }