from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model =Movie
        fields=('name','director','cast','description','plot','image','video','date')
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=('comment','rating')
