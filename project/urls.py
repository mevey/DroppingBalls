from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cw import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^votes$', views.votes, name='votes'),
    url(r'^info', views.info, name='info'),
    url(r'^cast-vote$', views.cast_vote, name='cast_vote'),
    url(r'^get-votes$', views.get_votes, name='get_votes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)