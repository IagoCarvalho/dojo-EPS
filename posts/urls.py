from django.conf.urls import url
from posts import views
from posts.views import PostsIndexView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^posts/$', views.PostsList.as_view()),
    url(r'^index/', PostsIndexView, name='PostsIndexView'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
