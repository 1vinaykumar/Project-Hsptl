from django.db import models
import datetime
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    userName=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
    address=models.TextField(max_length=150,default="N.A")
    blood_Group=models.CharField(max_length=10,default="N.A")
    bio=models.TextField(max_length=150,default="N.A")
    facebook=models.CharField(max_length=70,default="N.A")
    twitter=models.CharField(max_length=70,default="N.A")
    linkedIn=models.CharField(max_length=70,default="N.A")
    doB=models.DateField(default=datetime.date.today)
    priv=models.IntegerField(default=1)

class Appointment(models.Model):
    app_user=models.CharField(default='v',max_length=50)
    app_date=models.DateField(default=datetime.datetime.today)
    app_slot=models.IntegerField(default=1)
    app_doct=models.CharField(max_length=50,default='N.A')
    app_pay=models.BooleanField(default=False)
    app_pay_ref=models.CharField(max_length=25,default='N.A')
    app_prob=models.TextField(max_length=400,default='N.A')
    app_pri=models.IntegerField(default=1)
    app_status=models.IntegerField(default=2)


class Appoint(models.Model):
    app_dat=models.DateField(default=datetime.datetime.today)
    slots=models.IntegerField(default=0)

