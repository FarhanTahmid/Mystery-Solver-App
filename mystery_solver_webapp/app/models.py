from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Stories(models.Model):
    plot_of_the_murder=RichTextField(max_length=700,null=False,blank=False)
    whereabouts=RichTextField(max_length=1000,null=False,blank=False)
    evidence=RichTextField(max_length=1000,null=False,blank=False)
    class Meta:
        verbose_name="Mystery Stories"
    
    def __str__(self) -> str:
        return str(self.pk)

    