from django import forms

class MemeForm(forms.Form):

    template = forms.ChoiceField(choices=[
        ('drake.jpg', 'Drake'),
        ('distracted.jpg', 'Distracted Boyfriend'),
        # Add your templates here
    ]) 