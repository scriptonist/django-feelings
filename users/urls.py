from django.conf.urls import url, include
from . import views
urlpatterns = [
    url('^dashboard/$',views.dashboard,name='dashboard'),
    url('^', include('django.contrib.auth.urls'))
]
