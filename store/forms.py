from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
'''
# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
'''
#{{ content | safe }}