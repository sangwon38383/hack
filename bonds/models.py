from django.conf import settings 
from django.db import models
from django.utils import timezone  
from .text_analysis import *

class Bond(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)    
    company = models.TextField()
    roe = models.TextField()
    roa = models.TextField()
    debt_eq = models.TextField()
    long_debt_eq = models.TextField() 
    #gdp = models.TextField()
    #unemployment = models.TextField()
    #national_debt = models.TextField()
    #stock_market = models.TextField()
    estimated_rate = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    price = models.TextField()
    minprice = models.TextField(blank=True, null=True)
    
    def register(self):
        self.published_date = timezone.now()
        self.estimated_rate = do_anal(self.company)
        value = (1-float(self.estimated_rate))*float(self.price)
        self.save()

    def __str__(self):
        return self.company


class BondOther(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    company = models.TextField()
    roe = models.TextField()
    roa = models.TextField()
    debt_eq = models.TextField()
    long_debt_eq = models.TextField()
    #gdp = models.TextField()
    #unemployment = models.TextField()
    #national_debt = models.TextField()
    #stock_market = models.TextField()
    estimated_rate = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    price = models.TextField()
    bid = models.TextField(blank=True, null=True)

    def register(self):
        self.published_date = timezone.now()
        self.estimated_rate = do_anal(self.company)
        value = (1-float(self.estimated_rate))*float(self.price)
        self.save()

    def __str__(self):
        return self.company 
