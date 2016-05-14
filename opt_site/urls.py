from django.conf.urls import url

from opt_site.views import index, services, contact

urlpatterns = [
    # ex: /optimum/
    url(r'^home/', index, name='index'),
    url(r'^services/', services, name='services'),
    url(r'^contact/', contact, name='contact'),
]