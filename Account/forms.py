# from django import forms
# from .models import *
# from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(forms.Form):
#     first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Your First Name'
#     }))
#     last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Your Last Name'
#     }))
#     username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Enter your Username',
#         'autocomplete': 'off' 
#     }))
#     password1 = forms.CharField( max_length=40, label='Password' ,widget=forms.PasswordInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Enter Your Password',
#         'autocomplete': 'off'
#     }))
#     password2 = forms.CharField( max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Confirm Password',
#         'autocomplete': 'off'
#     }))

#     is_superuser = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
#         'class' : 'form-check-input'
#     }))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from Evaluate.models import Employee

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Enter Your Username'
#     }))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Enter Your Password'
#     }))

#     class Meta:
#         model = CustomUser
#         fields = ('username','password1')


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'First Name'
#     }))
#     last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Last Name'
#     }))
#     username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Username',
#         'autocomplete': 'off'
#     }))
#     password1 = forms.CharField( max_length=20, label='Password' ,widget=forms.PasswordInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Password',
#         'autocomplete': 'off'
#     }))
#     password2 = forms.CharField( max_length=20, label='Confirm Password', widget=forms.PasswordInput(attrs={
#         'class' : 'form-control',
#         'placeholder' : 'Confirm Password',
#         'autocomplete': 'off'
#     }))

#     class Meta:
#         model = CustomUser
#         fields = ('first_name','last_name','username','password1','password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'department', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'department': forms.Select(choices=CustomUser.DEP_CHOICES, attrs={
                'class' :'form-select'
            }),
            'role': forms.Select(choices=CustomUser.ROLE_CHOICES,attrs={
                'class' :'form-select'
            }),
        }

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['የሰራተኛው_ሙሉ_ስም', 'የቅርብ_ኃላፊው_ሙሉ_ስም', 'የስራ_መደቡ_መጠሪያ']
#         widgets = {
#             'የሰራተኛው_ሙሉ_ስም': forms.TextInput(attrs={'class': 'form-control'}),
#             'የቅርብ_ኃላፊው_ሙሉ_ስም': forms.TextInput(attrs={'class': 'form-control'}),
#             'የስራ_መደቡ_መጠሪያ': forms.TextInput(attrs={'class': 'form-control'}),
#         }