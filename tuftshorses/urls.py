from django.conf.urls import patterns, include, url
from horseshow.api import *
from django.conf.urls.defaults import *
from tastypie.api import Api
#from invitations.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

v1_api = Api(api_name='v1')
v1_api.register(HorseResource())
v1_api.register(HorseShowResource())
v1_api.register(RiderResource())
v1_api.register(ClassResource())
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
    url(r'^team/(?P<teamid>\d+)$', 'horseshow.views.team'),
    url(r'^team/(?P<teamid>\d+)/edit/$', 'horseshow.views.edit_team'),
    url(r'^region/(?P<regionid>\d+)$', 'horseshow.views.region'),
    url(r'^region/(?P<regionid>\d+)/edit/$', 'horseshow.views.edit_region'),
    url(r'^zone/(?P<zoneid>\d+)$', 'horseshow.views.zone'),
    url(r'^zone/(?P<zoneid>\d+)/edit$', 'horseshow.views.edit_zone'),
    url(r'^login', 'horseshow.views.not_user'),
    url(r'^user_login', 'horseshow.views.user_login'),
    url(r'^logout', 'horseshow.views.user_logout'),
    url(r'^show/(?P<showid>\d+)$', 'horseshow.views.show'),
    url(r'^invite/$','invitations.views.send_invite'),
    url(r'^invitation/(?P<invite_uuid>\w+)$','invitations.views.register'),
    url(r'^register/success/$','invitations.views.register_success'),
    url(r'^register/(?P<uuid>\w+)$','invitations.views.confirm_registration'),
    url(r'^user/edit/$','horseshow.views.edit_user'),
    url(r'^forgotpassword/$','invitations.views.forgot_password'),
    url(r'^forgotpassword/(?P<reset_uuid>\w+)$','invitations.views.reset_password'),
    url(r'^show/new/$','horseshow.views.new_show'),
    url(r'^show/(?P<showid>\d+)/create_classes$','horseshow.views.create_classes'),
    url(r'^show/(?P<showid>\d+)/edit$', 'horseshow.views.edit_show'),
    url(r'^roster/(?P<showteamid>\d+)/edit$','horseshow.views.edit_show_team'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #            {'document_root':settings.PROJECT_ROOT_PATH}),
    # url(r'^$', 'tuftshorses.views.home', name='home'),
    # url(r'^tuftshorses/', include('tuftshorses.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
