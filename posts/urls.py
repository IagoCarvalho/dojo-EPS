from django.conf.urls import url
from posts import views
from posts.views import PostsIndexView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^posts/$', views.posts_list),
    url(r'^index/', PostsIndexView, name='PostsIndexView'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
