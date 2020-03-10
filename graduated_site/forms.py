from django import forms
from .models import user_internship_post, comment, company, survey_model


class survey_form(forms.ModelForm):
    class Meta:
        model = survey_model
        fields=['name_surname', 'graduated_year', 'email', 'phone_number', 'graduated_program', 'adress', 'social_profile','graduated_state']

    def __init__(self, *args, **kwargs):
        super(survey_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['phone_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})


class internship_form(forms.ModelForm):
    class Meta:
        model = user_internship_post
        fields = ['title', 'image', 'content', 'company', 'adv_type', 'period_internship', 'time_internship',
                  'working_area', 'deadline']

    def __init__(self, *args, **kwargs):
        super(internship_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['deadline'].widget = forms.SelectDateWidget(attrs={'class': 'date-control'})


class adv_search(forms.Form):
    ad_type = (('all', 'Please select ad type'), ('0', 'INTERN'), ('1', 'WORK'))
    time_internship = (('all', 'Please select the internship duration'), ('30 DAYS', '30 DAYS'), ('60 DAYS', '60 DAYS'))
    period_internship = (
    ('all', 'Please select the internship period'), ('SUMMER', 'SUMMER'), ('WINTER', 'WINTER'), ('SPRING', 'SPRING'), ('AUTUMN', 'AUTUMN'))



    search = forms.CharField(required=False, max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))
    adv_type_search = forms.ChoiceField(label='Search by ad type',
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        choices=ad_type, required=True)
    time_internship_search = forms.ChoiceField(label='Search by internship duration',
                                               widget=forms.Select(attrs={'class': 'form-control'}),
                                               choices=time_internship, required=True)
    period_internship_search = forms.ChoiceField(label='Search by internship period',
                                                 widget=forms.Select(attrs={'class': 'form-control'}),
                                                 choices=period_internship, required=True)



class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(comment_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})


class company_form(forms.ModelForm):
    class Meta:
        model = company
        fields = ['company_name', 'company_type', 'company_sector', 'phone_number', 'adress']

    def __init__(self, *args, **kwargs):
        super(company_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['adress'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['phone_number'].widget = forms.NumberInput(attrs={'class': 'form-control'})
