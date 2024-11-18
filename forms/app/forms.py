from django import forms

class user_form(forms.Form):
    roll_num=forms.IntegerField()
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()