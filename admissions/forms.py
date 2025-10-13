from django import forms
from .models import Enquiry, Admission

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['student_name', 'guardian_name', 'phone_number', 'preferred_course']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter guardian name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'preferred_course': forms.Select(attrs={'class': 'form-control'}),
        }

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'surname', 'name', 'middlename', 'photo', 'contact_number', 
            'mobile_1', 'mobile_2', 'date_of_birth', 'mother_name', 
            'father_name', 'father_occupation', 'standard', 'batch', 
            'school_college', 'previous_percentage', 'stream'
        ]
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter surname'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter middle name (optional)'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'mobile_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter primary mobile number'}),
            'mobile_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter secondary mobile number (optional)'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother\'s name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father\'s name'}),
            'father_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father\'s occupation'}),
            'standard': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch'}),
            'school_college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school/college name'}),
            'previous_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter previous percentage', 'step': '0.01', 'min': '0', 'max': '100'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make stream field optional initially
        self.fields['stream'].required = False

class EnquiryUpdateForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['notes', 'followup_date', 'status']
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter notes'}),
            'followup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        } 