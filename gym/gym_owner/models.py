from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import STATE_CHOICES, GENDER_CHOICES
# importing signals
from django.dispatch import receiver
from django.db.models.signals import post_save


class BaseModel(models.Model):
    is_delete = models.IntegerField(null=False, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    changed_date = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.changed_date = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Address(BaseModel):

    id = models.AutoField(primary_key=True)
    building = models.CharField(max_length=30, null=False, blank=False)
    street = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    state = models.CharField(
        max_length=30, choices=STATE_CHOICES, null=False, blank=False)
    country = models.CharField(
        max_length=100, default="India", null=False, blank=False)

    def __str__(self):
        return f'{self.building}, {self.street}, {self.city}, {self.state}, {self.country}'

    class Meta:
        verbose_name_plural = "Address"


class Gym(BaseModel):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    contact = models.BigIntegerField(null=False, blank=False)
    gst_number = models.BigIntegerField(null=False, blank=False, default=None)
    email = models.CharField(max_length=30, null=True, blank=True)

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

    id = models.AutoField(primary_key=True)

    # Hacky solution.
    # We are creating first name  last name and email attribute on Owner class.
    # Why ?
    # So that we can make these field mandatory. User class does not make them
    # mandatory
    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        default="")
    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        default="")
    email = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        default="")

    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    # User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField('Address', on_delete=models.CASCADE)

    contact = models.CharField(max_length=10, null=False, blank=False)
    aadhar = models.CharField(max_length=10, null=False, blank=False)
    pan = models.CharField(max_length=20, null=False, blank=False)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        default=None,
        blank=True)

    profile_photo = models.ImageField(
        upload_to='static/images/gym_owner/profile',
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = "Owner"


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Owner.objects.create(user=instance)
    # instance.owner.save()


class Equipmet_MT(BaseModel):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=20, null=False)
    equipment_desc = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.equipment_name}'

    class Meta:
        verbose_name_plural = "Equipment_MT"


class Equipment_Details(BaseModel):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipmet_MT, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    count = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'{self.equipment.equipment_name} {self.count}'

    class Meta:
        verbose_name_plural = "Equipment_Details"


class Category_MT(BaseModel):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name_plural = "Category_MT"


class Diet(BaseModel):
    SHIFT_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('pre-workout', 'Pre-workout'),
        ('post-workout', 'Post-workout'),
    )

    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=False)
    category = models.ForeignKey(Category_MT, on_delete=models.CASCADE)
    shift = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        null=True,
        default=None)

    def __str__(self):
        return f'{self.name} - {self.category} - {self.shift}'

    class Meta:
        verbose_name_plural = "Diet"
