from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^posts/$', views.posts_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]
