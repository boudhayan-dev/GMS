from django.db import models
from gym_owner.models import Gym, BaseModel
from gym_customer.models import Customer
# Create your models here.


class Payment(BaseModel):

    id = models.CharField(max_length=50, primary_key=True)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    date = models.DateTimeField(null=False)

    class Meta:
        verbose_name_plural = "Payment"
