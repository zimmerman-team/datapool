from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views


admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^dolly_data','dp_management.views.get_dolly_data'),
    url(r'^tweets_per_day','dp_management.views.get_tweets_per_day'),
    url(r'^tweets_per_hour','dp_management.views.get_tweets_per_hour'),
    url(r'^top_twitter_users','dp_management.views.get_top_twitter_users'),
    url(r'^add_data','dp_management.views.add_data'),
    url(r'^add_project','dp_management.views.add_project'),
    url(r'^get_categories','dp_management.views.get_categories'),
    url(r'^save_property','dp_management.views.save_property'),
    url(r'^save_data_set','dp_management.views.save_data_set'),
    url(r'^save_project','dp_management.views.save_project'),
    url(r'^get_sub_categories/(?P<category_id>\w+)','dp_management.views.get_sub_categories'),
    url(r'^get_data_streams/(?P<sub_category_id>\w+)','dp_management.views.get_data_streams'),
    url(r'^delete_data_stream/(?P<id>\w+)','dp_management.views.delete_data_stream'),
    url(r'^delete_data_project/(?P<id>\w+)','dp_management.views.delete_data_project'),
    url(r'^get_queries/(?P<data_set_id>\w+)','dp_management.views.get_queries'),
    url(r'^visualize_project/(?P<project_id>\w+)','dp_management.views.visualize_project'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^', include('cms.urls')),


)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA


    

