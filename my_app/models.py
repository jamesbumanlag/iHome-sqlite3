from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=50)
    house_street = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    state  = models.CharField(max_length=20)
    post_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    med_background = models.CharField(max_length=250)
    care_plan = models.CharField(max_length=2500, null=True)
    contact_first = models.CharField(max_length=50)
    contact_last = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    contact_rel = models.CharField(max_length=20)
    person_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')



class PersonalCare(models.Model):
    
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    bathing = models.CharField(max_length=100)
    dressing = models.CharField(max_length=100)
    toileting = models.CharField(max_length=100)
    



class MobilityAssistance(models.Model):  
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    transfer = models.CharField(max_length=100)
    mobility = models.CharField(max_length=100)
    

    

class NutritionHydration(models.Model):
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    feeding_assistance = models.CharField(max_length=100)
    food_intake =models.CharField(max_length=100)
    fluid_intake = models.CharField(max_length=100)
    
    


class HealthMonitoring(models.Model):
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    bgl = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    o2 = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)


class Activities(models.Model):
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    companionship = models.CharField(max_length=100)
    daily_activities = models.CharField(max_length=100)


class Housekeeping(models.Model):
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    bathroom = models.CharField(max_length=100,default='Bathroom', null=True)
    laundry = models.CharField(max_length=100, default='Laundry',null=True)
    bedroom = models.CharField(max_length=100,  default='Bedroom',null=True)
    kitchen = models.CharField(max_length=100,  default='kitchen',null=True)
    living = models.CharField(max_length=100,  default='Living Room',null=True)
    
    
class CareType(models.Model):

    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    personal_care = models.CharField(max_length=100,default='Bathroom',)
    mobility_assistance = models.CharField(max_length=100,default='Bathroom',)
    nutrition_hydration = models.CharField(max_length=100,default='Bathroom',)
    health_monitoring = models.CharField(max_length=100,default='Bathroom',)
    activities = models.CharField(max_length=100,default='Bathroom',)
    housekeeping = models.CharField(max_length=100,default='Bathroom',)

    

class ProgressNotes(models.Model):

    CARE_TYPE_CHOICES = [
        ('personal_care','Personal Care' ),
        ('mobility_assistance','Mobility Assistance'),
        ('nutrition_hydration','Nutrition and Hydration'),
        ('health_monitoring','Health Monitoring'),
        ('activities','Activities'),
        ('housekeeping','Housekeeping'),

    ]
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, on_delete=models.CASCADE)
    care_types = models.CharField(max_length=20, choices=CARE_TYPE_CHOICES)
    progress_note = models.CharField(max_length=2500)