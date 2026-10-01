from django.db import models
from packages.models import Package
from teams.models import Team

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='assignments')

    staff = models.ForeignKey(
        Team, 
        on_delete=models.CASCADE, 
        related_name='assignments',
        limit_choices_to={'status': True, 'role__in': ['guide', 'porter']}
    )
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.staff.name} - {self.package.name}"