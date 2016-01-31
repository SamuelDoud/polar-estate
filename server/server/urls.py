from django.conf.urls import patterns, include, url
from django.contrib import admin
#we need to import each of our views from server.views as follows (or import *):
#from Dserver.views import
from Dserver.views import *
from django.conf.urls import patterns, url, include

admin.autodiscover()

# Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#patterns is a tuple of 2-tuples, each of which binds a partial url and a page view. 

urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)), (r'^page1/$', page1), (r'^API', API), (r'^UI/$', UI))

#, (r'^UI/$', UI)