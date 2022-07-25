from django import forms
from django.utils.safestring import mark_safe

class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=500, widget=forms.TextInput(attrs={'size':40, 'class':"searchbox"}))
    weight = forms.FloatField(label=mark_safe('<br><br>Strength (mg)'), required=False)
    country = forms.CharField(label=mark_safe("<br><br>Country:"), max_length=50, initial="Sri Lanka")
    area = forms.CharField(label=mark_safe("Area:"), max_length=50, initial="Colombo")