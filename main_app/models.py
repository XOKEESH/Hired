from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    application_date = models.DateField(auto_now_add=True)

    PENDING = 'Pending'
    APPLIED = 'Applied'
    INTERVIEWING = 'Interviewing'
    REJECTED = 'Rejected'
    OFFER_ACCEPTED = 'Offer Accepted'
    OFFER_DECLINED = 'Offer Declined'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPLIED, 'Applied'),
        (INTERVIEWING, 'Interviewing'),
        (REJECTED, 'Rejected'),
        (OFFER_ACCEPTED, 'Offer Accepted'),
        (OFFER_DECLINED, 'Offer Declined'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    job_link = models.URLField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'
    def get_absolute_url(self):
        return reverse('app-detail', kwargs={'app_id': self.id})
    