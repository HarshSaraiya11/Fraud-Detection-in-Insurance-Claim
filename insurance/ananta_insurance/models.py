from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class Claim(models.Model):

#     DRIVER_IS_CHOICES = (
#         ("owner", "owner"),
#         ("paiddriver","paiddriver"),
#         ("friend","friend"),
#         ("relative","relative")
#     )
#     ACCIDENT_TYPE_CHOICES = (
#         ("1","Single Vehicle Collision"),
#         ("2","Multi-Vehicle Collision"),
#         ("3","Parked Car"),
#         ("4","Vehicle Theft")
#     )
#     COLLISION_TYPE_CHOICES = (
#         ("0","Side Collision"),
#         ("1","Rear Collision"),
#         ("2","Front Collision"),
#         ("3","Other")
#     )
#     ACCIDENT_SEVERITY_CHOICES = (
#         ("0","Major Damage"),
#         ("1","Minor Damage"),
#         ("2","Total Loss"),
#         ("3","Trivial Damage")
#     )
#     DAMAGE_MATERIAL_CHOICES = (
#         ("Metal","Metal"),
#         ("Fiber","Fiber"),
#         ("Glass","Glass")
#     )
#     AUTH_CONTACTED_CHOICES = (
#         ("0","Police"),
#         ("1","Fire-Dept"),
#         ("2","Ambulance"),
#         ("3","Other"),
#         ("4","None")
#     )
#     POLICE_REPORT_CHOICES = (
#         ("0","Yes"),
#         ("1","No"),
#         ("2","N/A")
#     )
#     THIRD_PARTY_RESP_CHOICES = (
#         ("Yes","Yes"),
#         ("No","No")
#     )

#     fullname = models.CharField(max_length=25)
#     driver_is = models.CharField(max_length=20, choices=DRIVER_IS_CHOICES)
#     phone = models.BigIntegerField()
#     dlnumber = models.CharField(max_length=20)

#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=20)
#     stt = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     accident_type = models.CharField(max_length=20)
#     collision_type = models.CharField(max_length=20)
#     severity = models.CharField(max_length=20)
#     damage_material = models.CharField(max_length=20)
#     auth_contacted = models.CharField(max_length=20)
#     police_report = models.CharField(max_length=3)
#     fir = models.CharField(max_length=20)
#     third_party_resp = models.CharField(max_length=20)
#     noofvehicle = models.PositiveIntegerField()
#     noofpeople = models.PositiveIntegerField()
#     description = models.TextField(max_length=300)