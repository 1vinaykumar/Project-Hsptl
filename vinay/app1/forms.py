from django import forms
from .models import Register,Appoint,Appointment

class Login_form(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        #confirm_password = forms.CharField(widget=forms.PasswordInput)
        model=Register
        widgets= {
            'password': forms.PasswordInput(),
            'doB': forms.DateInput(attrs={'type': 'date', 'value': 'Date of Birth'}),
        }
        labels ={
            'doB': 'Date of Birth',
            'userName': 'User Name'
        }
        fields = [
            'name',
            'userName',
            'password',
            'doB',
            'email',
            'city',
            'mobile',
        ]

class Edit_form(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model=Register
        widgets= {
            'password': forms.PasswordInput(),
            'doB': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
            'address': forms.Textarea(attrs={'cols': 20, 'rows': 5})
        }
        labels ={
            'doB': 'Date of Birth',
            'userName': 'User Name',
            'blood_Group': 'Blood Group',
        }
        fields= [
            'name',
            'password',
            'email',
            'doB',
            'city',
            'mobile',
            'city',
            'blood_Group',
            'facebook',
            'twitter',
            'linkedIn',
            'address',
            'bio',

        ]

class Login(forms.Form):
    userName = forms.CharField(max_length = 30,required=True,label='User Name')
    password = forms.CharField(widget = forms.PasswordInput())

class Forgot_pass(forms.Form):
    userName = forms.CharField(max_length = 30,required=True,label='User Name')
    email = forms.EmailField(max_length = 50,required=True)
    mobile = forms.CharField(max_length = 12,required=True)


class Book_app(forms.ModelForm):
    class Meta:
        app_user = forms.CharField(widget=forms.HiddenInput(),label='')
        app_slot = forms.CharField(widget=forms.HiddenInput())
        model=Appointment
        widgets= {
            'app_date': forms.DateInput(attrs={'type': 'date'}),
            'app_user': forms.HiddenInput(),
            'app_slot': forms.HiddenInput(),
            'app_prob': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }
        labels ={
            'app_date': 'Appointment Date',
            'app_prob': 'Problem',
            'app_user': '',
            'app_slot': '',
        }
        fields= [
            'app_date',
            'app_prob',
            

        ]
    
