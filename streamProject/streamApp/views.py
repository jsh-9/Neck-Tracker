from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera
from .models import person
from django.conf import settings
import time

def index(request):
    return render(request, 'index2.html')

global Coordinates

def gen(cam):
    while True:
        frame, poses = cam.get_frame()
        settings.Coordinates = poses
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame
        time.sleep(0.05)

def gen2(cam):

    while True:
        frame, _= cam.get_frame()#get_position()#get_frame()
        # settings.Coordinates = poses
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame
        time.sleep(0.05)

def count(camera):
    yield camera.time_counter()

def get_position(flag, cam):
    frame, keypoint_list = cam.get_frame()
    if flag:
        del cam
        return keypoint_list
    else:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame


def get_posture(request, flag):
    if flag == 'False':
        return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')
    elif flag == 'True':
        poses = settings.Coordinates
        if not person.objects.filter(record_id="zjsh").exists():
            person_ = person(record_id="zjsh", x_nose=poses[0][0], y_nose= poses[0][1], x_shoulder= poses[1][0], y_shoulder= poses[1][1]) #(x_nose=3.22, y_nose= 3.22, x_shoulder=3.22, y_shoulder=3.22)#
            person_.save()

        return render(request, 'index.html')

def video_stream(request):
    # poses_ = person.objects.filter(record_id="zjsh").values()

    return StreamingHttpResponse(gen2(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def index2(request):
    return render(request, 'index.html')

