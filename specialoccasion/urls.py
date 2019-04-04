from django.conf.urls import url
from .views import specialoccasion

urlpatterns = [
    url(r'^$', specialoccasion, name='specialoccasion')
]