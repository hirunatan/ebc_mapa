from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name='index'),
    url(r"^csv/$", views.CSVView.as_view(), name='csv'),
    url(r"^organizacion/(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name='detail'),
    url(r"^organizacion/nueva/$", views.AddView.as_view(), name='add'),
    url(r"^organizacion/nueva-ok/$", views.AddOkView.as_view(), name='add-ok'),
]
