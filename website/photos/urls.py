from django.conf.urls  import url
from . import views

app_name= 'photos'

urlpatterns=[
#photos
  url(r'^$',views.index,name='index'),
  #photos/13
  url(r'^(?P<album_id>[0-9]+)$', views.detail ,name='detail'),
  #photos/album_id/favorite
  url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite ,name='favorite'),
]
