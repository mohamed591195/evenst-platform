from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Event(models.Model):
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events_created',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, blank=True)
    description = models.TextField()

    date = models.DateTimeField()

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='events_joined',
        related_query_name='event_joined',
        blank=True,
    ) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    @property
    def participants_count(self):
        return self.participants.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title
