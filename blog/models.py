from django.db import models
from django.urls import reverse

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('announcement-detail', kwargs={'pk': self.pk})

class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

class CourseOffer(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('course-offer-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)

class Faculty(models.Model):
    name = models.CharField(max_length=255)
    profile = models.TextField()
    contact_email = models.EmailField()
    image = models.ImageField(upload_to='faculty_images/', null=True, blank=True)

    def __str__(self):
        return self.name
