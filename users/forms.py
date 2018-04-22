from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = CustomUser 
		fields = UserCreationForm.Meta.fields
		
	
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields 
		
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email',)
		
class CustomuserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email', )