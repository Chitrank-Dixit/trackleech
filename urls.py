from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',#(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'static'})
    # Examples:
    url(r'^$', 'trackleech.blog.views.home', name='home'), # {'document_root':settings.STATIC_ROOT}
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
           { 'document_root': '/home/chitrank/Documents/Google_App_Engine/startup-repo/trackleech/static' }),
    # r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'static'}
    # url(r'','',)
    # url(r'^trackleech/', include('trackleech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
