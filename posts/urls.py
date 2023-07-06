# from django.conf.urls import url
# from . import views

# app_name = 'posts'

# urlpatterns = [
#     url(r'^$',views.posts, name='list'),
#     url(r'^create/$',views.post_create, name='create'),
#     url(r"^(?P<slug>[\w-]+)/$", views.post_detail, name='detail'),
# ]



from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='list'),
    path('create/', views.post_create, name='create'),
    path('<slug:slug>/', views.post_detail, name='detail'),
]
