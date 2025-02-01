from django.contrib import admin
from .models import Announcement, NewsPost, CourseOffer, Event, Faculty

admin.site.register(Announcement)
admin.site.register(NewsPost)
admin.site.register(CourseOffer)
admin.site.register(Event)
admin.site.register(Faculty)
