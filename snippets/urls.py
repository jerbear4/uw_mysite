from django.conf.urls import url
from snippets import views
from snippets.views import JSONResponse

urlpatterns = [
    url(r'^snippets/$', JSONResponse.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', JSONResponse.snippet_detail),
]