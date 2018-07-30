from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/profile/', views.new_profile, name='new-profile'),
    url(r'^new/picture/', views.upload_pic, name='new-picture'),
    url(r'^show/profile/(?P<user_id>\d+)', views.display_profile, name='show-profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^comment/(?P<picture_id>\d+)', views.addcomment, name='comment'),
    url(r'^follow/(?P<user_id>\d+)', views.follow, name='follow'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
