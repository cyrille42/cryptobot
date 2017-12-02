from django.conf.urls 	import url
from . 					import views

urlpatterns = [
    url(r'^alerts/$', views.AlertList.as_view(), name='alerts-list'),
    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^alerts/(?P<pk>[0-9]+)/$', views.AlertDetail.as_view(), name='alerts-detail'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='users-detail'),
    url(r'^rules/$', views.RuleList.as_view(), name='rules-list'),
    url(r'^rules/(?P<pk>[0-9]+)/$', views.RuleDetail.as_view(), name='rules-detail'),
]