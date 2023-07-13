from django import forms
from django.forms import ModelForm
from .models import lecture


week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
class LectureForm(ModelForm):
    class Meta:
        model = lecture
        fields = "__all__"
        labels={"subject":'',
            "prof":'',
            "day":'',
            "startTime":'',
            "endTime":'',
            "classroom":''}
        #hello
        widgets= {
            "subject":forms.TextInput(attrs={'class':'form-control','placeholder':'Subject Name'}),
            "prof":forms.TextInput(attrs={'class':'form-control','placeholder':'Professor Name'}),
            "day":forms.TextInput(attrs={'class':'form-control','placeholder':'Weekday'}),
            "startTime":forms.TimeInput(attrs={'type': 'time','class':'form-control','placeholder':'Start Time'}),
            "endTime":forms.TimeInput(attrs={'type': 'time','class':'form-control','placeholder':'End Time'}),
            "classroom":forms.NumberInput(attrs={'class':'form-control','placeholder':'Classroom Number'})
        }
