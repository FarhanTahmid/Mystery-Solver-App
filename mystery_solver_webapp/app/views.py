from django.shortcuts import render
from .models import Stories
from .bayesian_model import *
from django.http import JsonResponse
# Create your views here.

def welcome_view(request):
    # returns the welcome view of the screen
    return render(request,'index.html')

def stories(request,story_pk):
    # shows the stories and calls functions to resolve the stories    
    get_story=Stories.objects.get(pk=story_pk)
    
    context={
        'story':get_story,
    }
    
    if request.method=="POST":
        
        evidence={'Weapon':request.POST['weapon'],
            'Location':request.POST['location'],
            'Motive':request.POST['motive'],
            'Opportunity':request.POST['opportunity'],
        }
        query_vars = ['Farhan', 'Minhaz', 'Hasib', 'Fanna']
        
        results=BayesianModel.solve_mystery(evidence=evidence,query_vars=query_vars)
        
        inference_result={}
        for suspect, probs in results.items():
            for state, prob in probs.items():
                inference_result[suspect]={state:prob*100}
        
        
        max_value = float('-inf')
        potential_suspect = None

        for key, value in inference_result.items():
            if value[1] > max_value:
                max_value = value[1]
                potential_suspect = key

        return JsonResponse({'predictions':results,'potential_suspect':potential_suspect},safe=False)
                        
    return render(request,'stories.html',context=context)
    