from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interviewing'),
        ('offer', 'Offered'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    application_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
