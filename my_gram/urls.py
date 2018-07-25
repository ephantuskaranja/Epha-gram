from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^new/profile/', views.new_profile, name='new-profile'),
    url(r'^new/picture/', views.upload_pic, name='new-picture')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
