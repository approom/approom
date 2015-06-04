from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'approom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^account/", include("account.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
