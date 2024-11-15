from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company_name', 'position', 'application_date', 
            'status', 'follow_up_date', 'notes', 
            'resume', 'cover_letter'
        ]
        widgets = {
            'application_date': forms.SelectDateWidget(),
            'follow_up_date': forms.SelectDateWidget()
        }
