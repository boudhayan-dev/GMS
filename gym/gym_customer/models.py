from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from gym_owner.choices import GENDER_CHOICES

from gym_owner.models import Gym, Address, Diet, BaseModel


class Customer(BaseModel):
    # ID
    id = models.AutoField(primary_key=True)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    # User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    contact = models.BigIntegerField(null=False)
    aadhar = models.BigIntegerField(null=False)
    pan = models.CharField(max_length=20)
    dob = models.DateTimeField(null=False)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        default=None)

    profile_photo = models.ImageField(
        upload_to='static/images/gym_customer/profile',
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = "Customer"


class Diet_Subscription(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} subscribed to : {self.diet.name} diet plan'

    class Meta:
        verbose_name_plural = "Diet_Subscription"
