from django.conf.urls import patterns, include, url
from todoapp.views import next_view, all_task
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^index/(?P<user_id>\w+)$',next_view),
    url(r'^all$',all_task),
    url(r'^admin/', include(admin.site.urls))
)