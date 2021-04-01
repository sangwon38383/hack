from django.conf import settings 
from django.db import models
from django.utils import timezone  

#data_model = torch.load('')['model']
#data_model.cuda()

class Bond(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)    
    company = models.TextField()
    price = models.TextField() 
    roe = models.TextField()
    roa = models.TextField()
    debt_eq = models.TextField()
    long_debt_eq = models.TextField() 
    #gdp = models.TextField()
    #unemployment = models.TextField()
    #national_debt = models.TextField()
    #stock_market = models.TextField()
    #estimated_rate = models.TextField()
    #value = models.TextField()
    price = models.TextField(default = "none")
    
    def register(self):
        self.published_date = timezone.now()
        #self.estimated_rate = data_model.forward(self.roe, self.roa, self.debt_eq, self.long_debt_eq)        
        self.save()

    def __str__(self):
        return self.company

class BondOther(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    company = models.TextField()
    price = models.TextField()
    roe = models.TextField()
    roa = models.TextField()
    debt_eq = models.TextField()
    long_debt_eq = models.TextField()
    #gdp = models.TextField()
    #unemployment = models.TextField()
    #national_debt = models.TextField()
    #stock_market = models.TextField()
    #estimated_rate = models.TextField()
    #value = models.TextField()
    price = models.TextField(default = "none")

    def register(self):
        self.published_date = timezone.now()
        #self.estimated_rate = data_model.forward(self.roe, self.roa, self.debt_eq, self.long_debt_eq)
        self.save()

    def __str__(self):
        return self.company 
