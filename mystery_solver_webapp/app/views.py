from django.shortcuts import render

# Create your views here.

def welcome_view(request):
    # returns the welcome view of the screen
    return render(request,'index.html')

