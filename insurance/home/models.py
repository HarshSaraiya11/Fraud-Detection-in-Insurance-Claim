from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    phone = models.BigIntegerField(default="1111111111")
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    pan = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    policyno = models.CharField(max_length=6)
    premium = models.IntegerField()
    brand = models.CharField(max_length=15)
    caryear = models.CharField(max_length=4)
    registrationno = models.CharField(max_length=10)
    chassisno = models.CharField(max_length=17)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()