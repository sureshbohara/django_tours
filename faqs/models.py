from django.db import models

class Faq(models.Model):
    display_on = models.CharField(max_length=100, default='default')
    question = models.TextField()
    answer = models.TextField()
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level']

    def __str__(self):
        return self.question[:50]