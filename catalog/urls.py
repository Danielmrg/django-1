from django.conf.urls import url
from . import views
from catalog.views import Index
app_name = 'catalog'
urlpatterns = [
    # For Functional Base
    # url(r'^$', views.index , name='index')

    # For Class Base
    url(r'^$', Index.as_view(), name='index')
]
