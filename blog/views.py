from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Announcement, CourseOffer, Event, Faculty, NewsPost
from django.urls import reverse_lazy

class NewsPostDetailView(DetailView):
    model = NewsPost
    template_name = 'news_post_detail.html'

class CourseOfferListView(ListView):
    model = CourseOffer
    template_name = 'course_offer_list.html'

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'

class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty_list.html'

class NewsPostListView(ListView):
    model = NewsPost
    template_name = 'news_post_list.html'

class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'content']
    template_name = 'announcement_form.html'
    success_url = reverse_lazy('announcement-list')

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title', 'content']
    template_name = 'announcement_form.html'

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'announcement_confirm_delete.html'
    success_url = reverse_lazy('announcement-list')
class CourseOfferDetailView(DetailView):
    model = CourseOffer
    template_name = 'course_offer_detail.html'

class CourseOfferUpdateView(UpdateView):
    model = CourseOffer
    fields = ['course_name', 'description', 'availability']
    template_name = 'course_offer_form.html'
    success_url = reverse_lazy('course-offer-list')

class CourseOfferDeleteView(DeleteView):
    model = CourseOffer
    template_name = 'course_offer_confirm_delete.html'
    success_url = reverse_lazy('course-offer-list')
class CourseOfferCreateView(CreateView):
    model = CourseOffer
    fields = ['course_name', 'description', 'availability']
    template_name = 'course_offer_form.html'
    success_url = reverse_lazy('course-offer-list')
