from django.forms import ModelForm,  TextInput, Textarea, EmailInput
from .models import Job, Business


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description']
        widgets = {'title': TextInput(attrs={'class':'form-control'}),
                   'description': Textarea(attrs={'class':'form-control'})
        }

class BusinessRegistrationForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'address', 'city', 'state', 'zip_code', 'phone_number']
        widgets = {'name': TextInput(attrs={'class':'form-control'}),
                   'address': TextInput(attrs={'class':'form-control'}),
                   'city': TextInput(attrs={'class':'form-control'}),
                   'state': TextInput(attrs={'class':'form-control'}),
                   'zip_code': TextInput(attrs={'class':'form-control'}),
                   'phone_number': TextInput(attrs={'class':'form-control'})
        }

class JobSeekerEmailForm():
    fields = ['email']
    widgets = {'name': EmailInput(attrs={'class':'form-control'})}
