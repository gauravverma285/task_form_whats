from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Job(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    first_name = models.CharField(max_length=200, blank=True, null=True)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    countary = models.CharField(max_length=200, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    current_address = models.CharField(max_length=200, blank=True, null=True)
    project = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    number = models.IntegerField(max_length=10, blank=True, null=True)
    courses = models.ForeignKey('course', on_delete=models.CASCADE, blank=True, null=True)

    
    def __str__(self):
        return self.first_name

class course(models.Model):
    CERTIFICATION_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),
    )
    # job = models.ForeignKey('Job', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    certification = models.CharField(max_length=3, choices=CERTIFICATION_CHOICES, blank=True, null=True)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.title)

class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.full_name



