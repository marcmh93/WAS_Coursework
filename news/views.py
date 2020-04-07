from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import NewsStory


def index(request):
    latest_news_story = NewsStory.objects.order_by('-pub_date')
    context = {
        'latest_news_story': latest_news_story
    }
    return render(request,'news/index.html', context)

