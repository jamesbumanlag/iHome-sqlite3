from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, PersonalCare, MobilityAssistance, NutritionHydration, HealthMonitoring, Activities, Housekeeping, CareType, ProgressNotes
from django.forms import ModelForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	 

    

class AddRecordForm(forms.ModelForm):
    
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class': 'form-control','label':'' }))
    
    last_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class': 'form-control','label':'' }))
    age = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'','class': 'form-control', 'label':'' } ))
    gender = forms.CharField( required=True, widget=forms.widgets.TextInput( attrs={ 'placeholder':'', 'class': 'form-control','label':''  } ))
    religion = forms.CharField(required=True, widget=forms.widgets.TextInput( attrs={ 'placeholder':'','class': 'form-control', 'label':'' } ))
    
    house_street = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'','class': 'form-control',   'label':''  } ))
    suburb = forms.CharField(required=True, widget=forms.widgets.TextInput(  attrs={  'placeholder':'', 'class': 'form-control',  'label':''   }  ))
    state  = forms.CharField( required=True,widget=forms.widgets.TextInput(  attrs={'placeholder':'',  'class': 'form-control',   'label':''  }  ))
    post_code = forms.CharField( required=True, widget=forms.widgets.TextInput( attrs={ 'placeholder':'', 'class': 'form-control', 'label':'' } ))
    country = forms.CharField(required=True,  widget=forms.widgets.TextInput(attrs={  'placeholder':'', 'class': 'form-control','label':'' } ))
    
    section = forms.CharField(required=True, widget=forms.widgets.TextInput( attrs={ 'placeholder':'', 'class': 'form-control', 'label':''   }  ))
    med_background = forms.CharField( required=True,  widget=forms.widgets.TextInput(attrs={'placeholder':'','class': 'form-control', 'label':''  }  ))
    care_plan = forms.CharField( required=True,  widget=forms.widgets.Textarea(attrs={'placeholder':'','class': 'form-control', 'label':''  }  ))
   
    contact_first = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name', 'class': 'form-control', 'label':'' }  ))
    contact_last =forms.CharField( required=True,widget=forms.widgets.TextInput( attrs={ 'placeholder':'Last Name','class': 'form-control','label':'' } ))
    contact_number = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={ 'placeholder':'', 'class': 'form-control', 'label':'' } ))
    contact_rel = forms.CharField( required=True, widget=forms.widgets.TextInput( attrs={'placeholder':'', 'class': 'form-control', 'label':''  } ))
    person_image = forms.ImageField(required=False, )

    class Meta:
        model = Record
        exclude = ('user',)
        fields = '__all__'
        


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

class PersonalCareForms(forms.ModelForm):
    class Meta:
        model = PersonalCare
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    bathing = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Bath', 'class':'form-control', 'label':''}))
    dressing = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Dressing', 'class':'form-control', 'label':''}))
    toileting = forms.CharField(required=True, widget=forms.widgets.DateTimeInput(attrs={'placeholder':'Toileting', 'class':'form-control', 'label':''}))
    
class MobilityAssistanceForms(forms.ModelForm):
    class Meta:
        model = MobilityAssistance
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    transfer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Transfer', 'class':'form-control', 'label':''}))
    mobility = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Mobility', 'class':'form-control', 'label':''}))



class NutritionHydrationForms(forms.ModelForm):
    class Meta:
        model = NutritionHydration
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    food = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Food', 'class':'form-control', 'label':''}))
    feeding_assistance = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Assistance', 'class':'form-control', 'label':''}))
    fluid = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Fluid', 'class':'form-control', 'label':''}))



class HealthMonitoringForm(forms.ModelForm):
    class Meta:
        model = HealthMonitoring
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    bgl = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'bgL', 'class':'form-control', 'label':''}))
    bp = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Bp', 'class':'form-control', 'label':''}))
    o2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'o2', 'class':'form-control', 'label':''}))
    pulse = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Pulse', 'class':'form-control', 'label':''}))


class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    companion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Companionship', 'class':'form-control', 'label':''}))
    daily = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Daily Activities', 'class':'form-control', 'label':''}))



class HousekeepingForm(forms.ModelForm):
    class Meta:
        model = Housekeeping
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    bathroom = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Bathroom', 'class':'form-control', 'label':''}))
    laundry = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Laundry', 'class':'form-control', 'label':''}))
    bedroom = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Bedroom', 'class':'form-control', 'label':''}))
    kitchen = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Kitchen', 'class':'form-control', 'label':''}))
    living = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Living Room', 'class':'form-control', 'label':''}))



CARE_TYPE_CHOICES = [
    ('select', 'Select'),
    ('personal_care', 'Personal Care'),
    ('mobility_assistance', 'Mobility Assistance'),
    ('nutrition_hydration', 'Nutrition and Hydration'),
    ('health_monitoring', 'Health Monitoring'),
    ('activities', 'Activities'),
    ('housekeeping', 'Housekeeping'),
]



class ProgressNotesForm(forms.ModelForm):
    class Meta:
        model = ProgressNotes
        fields = '__all__'

    date = forms.DateField(widget=DateInput(attrs={'placeholder':'Date', 'class':'form-control', 'label':'Date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'placeholder':'Time', 'class':'form-control', 'label':'Time'}))
    person = forms.ModelChoiceField(queryset=Record.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Person")
    care_types = forms.ChoiceField( choices=CARE_TYPE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    progress_note = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder':'Write Progress Notes Here', 'class':'form-control', 'label':''}))
   
    