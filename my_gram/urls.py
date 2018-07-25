from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/profile/', views.new_profile, name='new-profile'),
    url(r'^new/picture/', views.upload_pic, name='new-picture'),
    url(r'^show/profile/(?P<user_id>\d+)', views.display_profile, name='show-profile'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
