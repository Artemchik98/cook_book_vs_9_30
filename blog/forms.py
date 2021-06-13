from django import forms
from  .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'id': 'nameInput'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'InputEmail',
            'aria-describedby': 'emailHelp'}))
    to = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'EmailTo'}))
    comment = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={
                                  'class': 'form-control',
                                  'id': 'comment',
                                  'rows': '3'}))


class CommentForm(forms.Form):
    name=forms.CharField(max_length=25,
                 widget=forms.TextInput(attrs={
                     'class':'form-control',
                     'id':'nameInput'}))
    email=forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputEmail',
            'aria-describedby':'emailHelp'}))
    comment=forms.CharField(
                    widget=forms.Textarea(attrs={
                    'class': 'form-control',
                    'id': 'comment',
                    'rows':3}))
