from django.conf.urls import include, url
from django.contrib import admin

from foobar import FooView

urlpatterns = [
    # Examples:
    # url(r'^$', 'drftest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^foo/', FooView.as_view(), name='api_foo'),
    url(r'^admin/', include(admin.site.urls)),
]
