from django import forms
class Postform(forms.Form):
	text=forms.CharField(label='Введи сообщение')
	file=forms.FileField()