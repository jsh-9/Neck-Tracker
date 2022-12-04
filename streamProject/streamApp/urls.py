from django.conf.urls.static import static
from django.urls import path
from .import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('video_stream', views.video_stream, name='video_stream'),
    path('(?P<flag>[-\w]+)/get_posture', views.get_posture, name='get_posture'),
    path('index2', views.index2, name='index2'),
    # path('paly_video', views.paly_video, name='paly_video')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)