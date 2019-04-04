"""wolfpreydigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from home import urls as home_urls
from dessert import urls as urls_dessert
from dinner import urls as urls_dinner
from baking import urls as urls_baking
from specialoccasion import urls as urls_specialoccasion
from blog import urls as urls_blog


urlpatterns = [
    url(r'^', include(home_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include(accounts_urls)),
    url(r'^dessert/',include(urls_dessert)),
    url(r'^dinner/',include(urls_dinner)),
    url(r'^baking/',include(urls_baking)),
    url(r'^specialoccasion/',include(urls_specialoccasion)),
    url(r'^blog/',include(urls_blog)),
]
