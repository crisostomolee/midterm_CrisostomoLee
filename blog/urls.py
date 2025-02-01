from django.urls import path
from .views import (
    NewsPostListView,
    NewsPostDetailView,
    CourseOfferListView,
    EventListView,
    FacultyListView,
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    CourseOfferUpdateView,
    CourseOfferDetailView,
    CourseOfferDeleteView,
    CourseOfferCreateView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('courses/new/', CourseOfferCreateView.as_view(), name='course-offer-create'),
    path('courses/<int:pk>/', CourseOfferDetailView.as_view(), name='course-offer-detail'),
    path('courses/<int:pk>/edit/', CourseOfferUpdateView.as_view(), name='course-offer-update'),
    path('courses/<int:pk>/delete/', CourseOfferDeleteView.as_view(), name='course-offer-delete'),
    path('courses/', CourseOfferListView.as_view(), name='course-offer-list'),
    path('news/<int:pk>/', NewsPostDetailView.as_view(), name='news-post-detail'),
    path('news/', NewsPostListView.as_view(), name='news-post-list'),
    path('courses/', CourseOfferListView.as_view(), name='course-offer-list'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('faculty/', FacultyListView.as_view(), name='faculty-list'),
    path('', AnnouncementListView.as_view(), name='announcement-list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('new/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('<int:pk>/edit/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
