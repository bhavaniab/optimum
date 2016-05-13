from django.conf.urls import url

from opt_site.views import index

urlpatterns = [
    # ex: /optimum/
    url(r'^home/', index, name='index'),
]