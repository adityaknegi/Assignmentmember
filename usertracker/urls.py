from django.conf.urls import url
from usertracker import views

urlpatterns = [
    url(r'^api/usertracker/user$', views.user_validator),
    url(r'^api/usertracker/user_activity/(?P<user_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})'
        r'/(?P<user_hash>\w+)$', views.user_activity, name='user_activity'),
    url(r'^api/usertracker/get_members$', views.get_members, name='get_members')
]