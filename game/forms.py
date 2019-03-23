from django import forms
from .models import Reviews, GameEvents, Games

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

class GameForm(forms.ModelForm):
    class Meta:
        model=Games
        fields='__all__'

