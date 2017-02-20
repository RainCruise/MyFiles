from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index.html/$', views.index),
    url(r'^about_us.html/$', views.about_us),
    url(r'^join_us_dars.html/$', views.join_us_dars),
    url(r'^join_us_szqt.html/$', views.join_us_szqt),
]
