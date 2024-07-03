from django import forms
from .models import CVResume, PersonalInfo, Education, WorkExperience, Certification, Skill



class CVResumeForm(forms.Form):
    # Personal Information Fields
    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    nationality = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Education Fields
    education_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    field_of_study = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    graduation_year = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Work Experience Fields
    company = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    responsibilities = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Certification Fields
    certification_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    issuer_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    certification_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    # Skills Fields (ManyToMany)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control'}))


