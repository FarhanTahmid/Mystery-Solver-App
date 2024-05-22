from django.urls import path
from . import views

app_name="app"

urlpatterns = [
    path('',views.welcome_view,name="welcome_view"),
    path('story/<int:story_pk>',views.stories,name="story"),
]
