from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>\w+)/$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^comment/$', views.CommentCreateView.as_view(), name='comment-create'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.CommentListView.as_view(), name='comment-list'),
]
