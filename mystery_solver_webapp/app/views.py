from django.shortcuts import render
from .models import Stories
# Create your views here.

def welcome_view(request):
    # returns the welcome view of the screen
    return render(request,'index.html')

def stories(request,story_pk):
    # shows the stories and calls functions to resolve the stories
    
    get_story=Stories.objects.get(pk=story_pk)
    
    print(get_story.plot_of_the_murder)
    return render(request,'stories.html')
    