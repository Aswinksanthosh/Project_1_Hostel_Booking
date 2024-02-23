from django.db import models

# Create your models here.
class User_registration(models.Model):
    phno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    gmail=models.EmailField()
    pwd=models.CharField(max_length=20)
    ck_in=models.DateField(blank=True,null=True)
    ck_out=models.DateField(blank=True,null=True)
    price_paid=models.IntegerField(blank=True,null=True)
    sharing=models.CharField(blank=True,null=True,max_length=10)
    h_id=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return (self.name)

class hostels(models.Model):
    h_id=models.IntegerField(primary_key=True,blank=True)
    price4=models.IntegerField()
    price6=models.IntegerField()
    price8=models.IntegerField()
    price10=models.IntegerField()
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=400)
    rating=models.FloatField(blank=True,null=True)
    share4=models.IntegerField()
    share6=models.IntegerField()
    share8=models.IntegerField()
    share10=models.IntegerField()
    address=models.TextField(max_length=50)
    phno=models.IntegerField()
    img=models.FileField(null=True)
    gmail=models.EmailField()
    def __str__(self):
        return self.name

class admin_reg(models.Model):
    phno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    gmail=models.EmailField()
    pwd=models.CharField(max_length=20)
    h_id=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return (self.name)