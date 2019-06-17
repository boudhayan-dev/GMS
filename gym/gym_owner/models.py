from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    is_delete = models.IntegerField(null=False, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    changed_date  = models.DateTimeField(blank=True, null=True)


    def update(self):
        self.changed_date = timezone.now()
        self.save()

    class Meta:
        abstract = True 


class Address(BaseModel):
    id = models.AutoField(primary_key=True)
    building = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20, null = False)
    state = models.CharField(max_length=20, null = False)
    country = models.CharField(max_length=100, default="India")

    def __str__(self):
        return f'{self.building}, {self.street}, {self.city}, {self.state}, {self.country}'

    
    class Meta:
        verbose_name_plural = "Address"




class Gym(BaseModel):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.BigIntegerField(null=False)
    gst_number = models.BigIntegerField(null=True, default=None)
    email = models.CharField(max_length = 30, null= True)
    
    address = models.OneToOneField('Address', on_delete=models.CASCADE)

    

    # def update(self):
    #     self.changed_date = timezone.now()
    #     self.save()

    def __str__(self):
        return f'Gym : {self.name}, Contact : {self.contact}, Address : {self.address}'

    class Meta:
        verbose_name_plural = "Gym"



class Owner(BaseModel):
    # ID
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others'),
    )

    id = models.AutoField(primary_key=True)
    gym = models.ForeignKey(Gym, on_delete = models.CASCADE)
    # User model
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)

    contact =  models.BigIntegerField(null=False)
    aadhar =  models.BigIntegerField(null=False)
    pan = models.CharField(max_length=20)
    dob = models.DateTimeField(null=False)
    gender =  models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, default=None)

    profile_photo = models.ImageField( upload_to='static/images/gym_owner/profile', null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


    class Meta:
        verbose_name_plural = "Owner"




class Equipmet_MT(BaseModel):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=20, null = False)
    equipment_desc = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.equipment_name}'

    class Meta:
        verbose_name_plural = "Equipment_MT"


class Equipment_Details(BaseModel):
    gym = models.ForeignKey(Gym,on_delete = models.CASCADE)
    equipment = models.ForeignKey(Equipmet_MT, on_delete = models.CASCADE)
    id = models.AutoField(primary_key=True)

    count = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'{self.equipment.equipment_name} {self.count}'
    
    class Meta:
        verbose_name_plural = "Equipment_Details"



class Category_MT(BaseModel):
    id = models.AutoField(primary_key=True)
    category =  models.CharField(max_length=20, null= False)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name_plural = "Category_MT"



class Diet(BaseModel):
    SHIFT_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner','Dinner'),
        ('pre-workout','Pre-workout'),
        ('post-workout','Post-workout'),
    )

    gym = models.ForeignKey(Gym,on_delete = models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null= False)
    description = models.CharField(max_length=500, null= False)
    category = models.ForeignKey(Category_MT, on_delete = models.CASCADE)
    shift =  models.CharField(max_length=20, choices=SHIFT_CHOICES, null=True, default=None)


    def __str__(self):
        return f'{self.name} - {self.category} - {self.shift}'

    class Meta:
        verbose_name_plural = "Diet"


