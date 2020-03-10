from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, user_work_company, user_message_box
from django.contrib.auth import authenticate
import re


class register_form(forms.ModelForm):
    password = forms.CharField(required=True, label='Password', min_length=6, max_length=25,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(required=True, label='Confirm Password', min_length=6, max_length=25,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=6, required=True, label='Student Number',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            self.add_error('password', 'Passwords did not match')
            self.add_error('password_confirm', 'Passwords did not match')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '':
            raise forms.ValidationError('Please enter e-mail')
        email = email.lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This e-mail is registered in the system')
        return email

    def clean_username(self):
        student_number = self.cleaned_data.get('username')
        if User.objects.filter(username=student_number).exists():
            raise forms.ValidationError('This student number is registered in the system')
        return student_number


class login_form(forms.Form):
    username = forms.CharField(label='Student Number or E-mail', required=True, max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, max_length=25, min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('<b>Incorrect student number or password</b>')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            users = User.objects.filter(email__iexact=username)
            if len(users) > 0 and len(users) == 1:
                return users.first().username
        return username


class userprofile_update_form(forms.ModelForm):
    birth_date = forms.DateField(input_formats=("%d.%m.%Y",), widget=forms.DateInput(format="%d.%m.%Y"),
                                 label='Birthdate')
    graduated_date = forms.DateField(input_formats=("%d.%m.%Y",), widget=forms.DateInput(format="%d.%m.%Y"), label='Graduation Day')
    first_day = forms.DateField(input_formats=("%d.%m.%Y",), widget=forms.DateInput(format="%d.%m.%Y"), label='Your First Day In Company')
    last_day = forms.DateField(input_formats=("%d.%m.%Y",), widget=forms.DateInput(format="%d.%m.%Y"), label='Your Last Day In Company')

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_photo', 'working_area', 'working_position', 'foreign_language', 'certificate',
                  'education', 'birth_date', 'company', 'first_day', 'last_day', 'graduated_date']

    def __init__(self, *args, **kwargs):
        super(userprofile_update_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['bio'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['education'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['certificate'].widget = forms.Textarea(attrs={'class': 'form-control'})
        DATEPICKER = {
            'type': 'text',
            'class': 'form-control',
            'id': 'datetimepicker1',
            'autocomplete': 'off'
        }
        self.fields['birth_date'].widget.attrs.update(DATEPICKER)
        self.fields['graduated_date'].widget.attrs.update(DATEPICKER)
        self.fields['first_day'].widget.attrs.update(DATEPICKER)
        self.fields['last_day'].widget.attrs.update(DATEPICKER)


class user_work_company_form(forms.ModelForm):
    class Meta:
        model = user_work_company
        fields = ['company', 'first_day']

    def __init__(self, *args, **kwargs):
        super(user_work_company_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

class message_box_form(forms.ModelForm):
    class Meta:
        model = user_message_box
        fields = ['to_user', 'message_title', 'message']

    def __init__(self, *args, **kwargs):
        super(message_box_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['message'].widget = forms.Textarea(attrs={'class': 'form-control'})


