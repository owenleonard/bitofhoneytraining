from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'(?i)directions$', 'directions'),
    url(r'(?i)facilities$', 'facilities'),
    url(r'(?i)lesson_horses$', 'lesson_horses'),
    url(r'(?i)horses_for_sale/dream$', 'dream'),
    url(r'(?i)horses_for_sale/dewey$', 'dewey'),
    url(r'(?i)pictures$', 'pictures'),
    url(r'(?i)reading$', 'reading'),
    url(r'(?i)services$', 'services'),
    url(r'(?i)trainer$', 'trainer'),
    url(r'(?i)testimonials$', 'testimonials'),
    url(r'(?i)pt$', 'pt'),
    url(r'(?i)holistic$', 'holistic'),
    url(r'(?i)fitting$', 'fitting'),
    url(r'(?i)consulting$', 'consulting'),
    url(r'(?i)instruction$', 'instruction'),
    url(r'(?i)calendar$', 'calendar'),
    url(r'(?i)estimator$', 'estimator'),
)

