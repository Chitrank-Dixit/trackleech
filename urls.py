from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

'''
using urls.py: This files specifies all the files that would be connected when called through
any hyper-reference and this like
url(r'^$', 'trackleech.blog.views.home', name='home') 
arg 1 shows find the page in blog and thus nothing is specified that means to search for index.html
arg 2 takes full heirarchy of the django filesystem and 
arg 3 takes name argument 

url(r'^blog/', 'trackleech.blog.views.search', name='search'),



'''

urlpatterns = patterns('',#(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'static'})
    # Examples:
    url(r'^$', 'trackleech.blog.views.home', name='home'), # {'document_root':settings.STATIC_ROOT}
    url(r'^blog/', 'trackleech.blog.views.search', name='search'),
    url(r'^blog/', 'trackleech.blog.views.profile', name='profile'),
    url(r'^signup/', 'trackleech.blog.views.signup',name='signup'),
    url(r'^signin/', 'trackleech.blog.views.signin',name='signin'),
    url(r'^signout/', 'trackleech.blog.views.signout',name = 'signout'),
    
    # url(r'^blog/', 'trackleech.blog.views.search', name='search'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/home/chitrank/Documents/Google_App_Engine/startup-repo/trackleech/static' }),
    # r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'static'}
    # url(r'','',)
    # url(r'^trackleech/', include('trackleech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
