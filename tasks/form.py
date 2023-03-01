from django import forms
from .models import task


class taskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'descrition', 'important']
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"write a title"}),
            "descrition": forms.Textarea(attrs={"class":"form-control", "placeholder":"write a description"}), 
            "important": forms.CheckboxInput(attrs={"class":"form-check-input m-auto", }), 
        }