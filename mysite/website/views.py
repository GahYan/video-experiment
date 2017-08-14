from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Video
# Create your views here.
def home(request):
    template = loader.get_template('website/homepage.html')
    context={}
    return HttpResponse(template.render(context, request))
def everything(request):
    video_list= Video.objects.all()
    template = loader.get_template('website/everything.html')
    context = {
        'video_list': video_list,
        }
    return HttpResponse(template.render(context, request))
def preferences(request):
    video_list= Video.objects.all()
    unwanted_list=request.POST.getlist('unwanted')
    wanted_list=request.POST.getlist('wanted')
    template = loader.get_template('website/preferences.html')
    wanted_videos=[]
    for video in video_list:
        for tag in video.tags.all():
            if tag.name in unwanted_list:
                break
        else:
            for tag in video.tags.all():
                if tag.name in wanted_list:
                    wanted_videos.append(video)
                    break

    context={
    'video_list':video_list,
    'unwanted_list':unwanted_list,
    'wanted_list':wanted_list,
    'wanted_videos':wanted_videos
    }
    return HttpResponse(template.render(context, request))
