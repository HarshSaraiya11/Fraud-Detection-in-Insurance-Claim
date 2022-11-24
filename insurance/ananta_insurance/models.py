from django.db import models

# Create your models here.
# class Claim(models.Model):
#     fullname = models.CharField(max_length=25)
#     driver_is = models.CharField(max_length=20)
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
#     police_report = models.CharField(max_length=20)
#     fir = models.CharField(max_length=20)
#     third_party_resp = models.CharField(max_length=20)
#     noofvehicle = models.IntegerField()
#     noofpeople = models.IntegerField()
#     description = models.TextField()