from django import forms
from question.models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields  = ('username','password')












