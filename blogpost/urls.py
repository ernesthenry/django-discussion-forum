# from django.conf.urls import url, include
# from django.contrib import admin
# from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings
# # from posts import views as post_views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^about/$', views.about),
#     # url(r'^$',post_views.posts, name="home"),
#     url(r'^accounts/',include('accounts.urls')),
#     url(r'^posts/',include('posts.urls')),
# ]

# urlpatterns +=staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    # path('', post_views.posts, name="home"),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 