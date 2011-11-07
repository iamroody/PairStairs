from django.conf.urls.defaults import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pairstairs.views',
    (r'^$', 'stairs'),
    (r'^add$', 'add'),
    (r'^(?P<firstMember_id>.+?)/(?P<secondMember_id>.+?)$', 'add_count')
)