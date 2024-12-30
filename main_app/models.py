from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
timezone.now


# Create your models here.

# class App(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=200)
#     application_date = models.DateField(auto_now_add=True)

#     PENDING = 'Pending'
#     APPLIED = 'Applied'
#     INTERVIEWING = 'Interviewing'
#     REJECTED = 'Rejected'
#     OFFER_ACCEPTED = 'Offer Accepted'
#     OFFER_DECLINED = 'Offer Declined'

#     STATUS_CHOICES = [
#         (PENDING, 'Pending'),
#         (APPLIED, 'Applied'),
#         (INTERVIEWING, 'Interviewing'),
#         (REJECTED, 'Rejected'),
#         (OFFER_ACCEPTED, 'Offer Accepted'),
#         (OFFER_DECLINED, 'Offer Declined'),
#     ]

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default=PENDING,
#     )

#     job_link = models.URLField(blank=True, null=True)
#     job_description = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

#     def __str__(self):
#         return f'{self.job_title} at {self.company_name}'
#     def get_absolute_url(self):
#         return reverse('app-detail', kwargs={'app_id': self.id})
    
class App(models.Model):
    # Metadata
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    application_date = models.DateField()

    # Status Choices
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
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

    class Meta:
        ordering = ['-application_date']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'

    def get_absolute_url(self):
        return reverse('app-detail', kwargs={'pk': self.id})

class Interview(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='interviews')
    date = models.DateTimeField('Interview Date')
    type = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Interview on {self.date} for {self.app}'
    
    class Meta:
        ordering = ['-date']

class Note(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='notes')
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'Note for {self.app} on {self.created_at}'
    
    class Meta:
        ordering = ['-created_at']

class Task(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='tasks')
    task_description = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Task: {self.description} for {self.app}'

class FollowUp(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='followups')
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'FollowUp on {self.date} for {self.app}'
    
    class Meta:
        ordering = ['-date']

class Contact(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    contact_date = models.DateField(blank=True, null=True)
    contact_notes = models.TextField(blank=True, null=True)
    contact_method = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Contact: {self.name} for {self.app}'

class Feedback(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='feedback')
    date = models.DateField()
    comments = models.TextField()

    def __str__(self):
        return f'Feedback for {self.app} on {self.date}'
    
    class Meta:
        ordering = ['-date']

class Offer(models.Model):
    app = models.OneToOneField(App, on_delete=models.CASCADE, related_name='offer')
    offer_details = models.TextField()
    offer_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        status = "Accepted" if self.accepted else "Declined"
        return f'Offer ({status}) for {self.app} - Salary: {self.salary}'