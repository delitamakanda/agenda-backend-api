from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^events$', views.EventListView.as_view(), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event-detail'),
    url(r'^event-guest$', views.EventGuestListView.as_view(), name='eventguest-list'),
    url(r'^event-guest/(?P<pk>\d+)/$', views.EventGuestDetailView.as_view(), name='eventguest-detail'),
]
