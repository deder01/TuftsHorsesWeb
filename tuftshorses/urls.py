from django.conf.urls import patterns, include, url
from horseshow.api import *
from django.conf.urls.defaults import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(HorseResource())
v1_api.register(HorseShowResource())
v1_api.register(RiderResource())
v1_api.register(DivisionResource())
v1_api.register(TeamResource()) 
v1_api.register(UserResource())
v1_api.register(ShowTeamResource())
v1_api.register(MembershipResource())
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^api/',include(v1_api.urls)),
    url(r'^$', 'horseshow.views.home'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root':settings.STATIC_ROOT}),
    # url(r'^$', 'tuftshorses.views.home', name='home'),
    # url(r'^tuftshorses/', include('tuftshorses.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
