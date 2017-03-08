from django.conf.urls import url
from snippets import views
from snippets.views import JSONResponse

urlpatterns = [
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/$', views.snippet_list),
]