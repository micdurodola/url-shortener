from django import forms
from .models import short_urls

#Enter For  Parameters
class UrlForm(forms.ModelForm):

    class Meta:
        model = short_urls
        fields = ['long_url']
