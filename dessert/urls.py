from django.conf.urls import url
from .views import dessert

urlpatterns = [
    url(r'^$', dessert, name='dessert')
]