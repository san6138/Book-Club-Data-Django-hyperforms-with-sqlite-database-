from django import forms

class Registrationform(forms.Form):
    name = forms.CharField(label='your name', max_length=100)
    age = forms.IntegerField(label='your age')
    favorite_book = forms.CharField(label='your favorite book', max_length=100)