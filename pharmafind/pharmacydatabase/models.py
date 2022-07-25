from operator import mod
from statistics import mode
from tkinter import CASCADE
from django.db import models
from matplotlib import mlab
from pages.models import PharmacyManager

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class DrugType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=50, default="")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    drugtype = models.ForeignKey(DrugType, on_delete=models.CASCADE)
    milligrams = models.FloatField(blank=True, null=True)

    def __str__(self):
        if str(self.brand) == "No brand":
            return self.drugtype.name + " with no brand, and a strength of " + str(self.milligrams) + "mg"
        else:
            return self.drugtype.name + " of brand " + self.brand.name + " with a strength of " + str(self.milligrams) + "mg"

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null= True)
    contactemail = models.EmailField(max_length=50, blank=True, null= True)
    website = models.CharField(max_length=50, blank=True, null= True)
    delivery = models.BooleanField()
    canimport = models.BooleanField()
    country = models.CharField(max_length=50, default="")
    area = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    gmaplink = models.CharField(max_length=300, default='https://maps.google.com')
    pharmacymanager = models.ForeignKey(PharmacyManager, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(s):
        if "pharmacy" in s.name.lower():
            return s.name
        else:
            return s.name + "Pharmacy"

class DrugSet(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.count) + ' x "' + str(self.drug) + '", (in  pharmacy "' + self.pharmacy.name +'")'

