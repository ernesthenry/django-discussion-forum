from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',views.posts, name='list'),
    url(r'^create/$',views.post_create, name='create'),
    url(r"^(?P<slug>[\w-]+)/$", views.post_detail, name='detail'),
]
