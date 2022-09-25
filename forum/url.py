from django.conf.urls.static import static
from django.urls import path

from config import settings
from forum.views import *

urlpatterns = [
    path('', main, name='main_page'),
    path('card/<int:id>', video, name='card'),
    path('download<str:name>', video, name='download'),
    path('post', post, name='post')

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
