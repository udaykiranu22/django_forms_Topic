from django import forms
from app.models import *
class ContactForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


class TopicForm(forms.Form):
    topic_name = forms.CharField()

class WebpageForm(forms.Form):
    topic_name = forms.ModelChoiceField(queryset = Topic.objects.all())
    name = forms.CharField()
    url = forms.URLField()

class AccessRecord(forms.Form):
    name = forms.ModelChoiceField(queryset = Webpage.objects.all())
    author = forms.CharField()
    date = forms.DateField()

