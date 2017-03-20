from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.Photo_upload, name = 'Photo_upload'),

	url(r'^photoloading', views.Photoloading, name = 'Photoloading'),

	url(r'^mystarface', views.Mystarface, name = 'Mystarface'),

	url(r'^registration/$', views.post2db, ),

	url(r'^matchlist/$', views.matchlist),

	url(r'^loading/$', views.Loading),

	url(r'^choosegirl/$', views.Choosegirl),

	url(r'^chooseboy/$', views.Chooseboy),

	url(r'^accountinfo/(?P<id>.*)$', views.AccountInfo, name= 'AccountInfo'),

	url(r'^test/$', views.your_view, name= 'your_view'),

]
