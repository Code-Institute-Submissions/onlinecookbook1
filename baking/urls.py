from django.conf.urls import url
from .views import baking

urlpatterns = [
    url(r'^$', baking, name='baking')
]