from django.conf.urls import url
from .views import dinner

urlpatterns = [
    url(r'^$', dinner, name='dinner')
]